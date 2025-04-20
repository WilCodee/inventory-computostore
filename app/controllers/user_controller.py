import bcrypt

from app.database.connect_mongo import ConnectMongo
from app.models.user import User


class UserController:
    @staticmethod
    def to_dict(user: User):
        return {
            "username": user.username,
            "password_hash": user.password_hash,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "date_creation": user.date_creation,
            "status": user.status
        }

    @staticmethod
    def save_user(collection, user: User):
        user_dict = UserController.to_dict(user)  # Convierte el objeto en un diccionario
        result = collection.insert_one(user_dict)  # Inserta el usuario
        return result.inserted_id  # Devuelve el ID del nuevo documento

    @staticmethod
    def create_user(username, password, name, email):
        # Verificar si el nombre de usuario ya existe
        connection = ConnectMongo()
        collection = connection.get_collection("users")

        # Comprobar si el usuario ya existe en la base de datos
        if collection.find_one({"username": username}):
            connection.close_connection()
            return {"error": "El nombre de usuario ya está en uso."}

        # Hashear la contraseña
        hashed_password = UserController.hash_password(password)

        # Crear el usuario
        user = User(username=username, password_hash=hashed_password, name=name, email=email)

        # Guardar el usuario en la base de datos
        user_id = UserController.save_user(collection, user)

        connection.close_connection()

        # Retornar el ID del usuario creado
        return {"success": f"Usuario creado con ID: {user_id}"}

    @staticmethod
    def verification_user(username, password):
        # Buscar el usuario por nombre de usuario
        connection = ConnectMongo()
        collection = connection.get_collection("users")

        user = collection.find_one({"username": username})

        if not user:
            connection.close_connection()
            return {"error": "Usuario no encontrado."}

        # Verificar la contraseña
        if UserController.verification_password(user["password_hash"], password):
            connection.close_connection()
            return {"success": "Acceso exitoso."}
        else:
            connection.close_connection()
            return {"error": "Contraseña incorrecta."}

    @staticmethod
    def hash_password(password):
        # Genera un salt
        salt = bcrypt.gensalt()
        # Hashea la contraseña
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    @staticmethod
    def verification_password(stored_hash, password):
        # Verifica si la contraseña coincide con el hash almacenado
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
