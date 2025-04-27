import bcrypt

from app.database.connect_mongo import ConnectMongo
from app.exceptions.auth_exceptions import UserAlreadyExistsError, UserNotFoundError, IncorrectPasswordError, \
    UserInactiveError
from app.models.user import User
from app.utils.validators import AuthValidators


class UserController:
    @staticmethod
    def __to_dict(user: User) -> dict:
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
    def __insert_user(collection: [], user: User) -> None:
        user_dict = UserController.__to_dict(user)  # Convierte el objeto en un diccionario
        collection.insert_one(user_dict)  # Inserta el usuario

    @staticmethod
    def create_user(username: str, password: str, name: str, email: str) -> None:
        email = AuthValidators.validate_email(email)

        connection = ConnectMongo()
        try:
            collection = connection.get_collection("users")

            # Comprobar si el usuario ya existe en la base de datos
            if collection.find_one({"username": username}):
                raise UserAlreadyExistsError()

            # Hashear la contraseña
            hashed_password = UserController.__hash_password(password)

            # Crear el usuario
            user = User(username=username, password_hash=hashed_password, name=name, email=email)

            # Guardar el usuario en la base de datos
            UserController.__insert_user(collection, user)
        finally:
            connection.close_connection()

    @staticmethod
    def verification_user(username: str, password: str) -> bool:
        connection = ConnectMongo()
        try:
            collection = connection.get_collection("users")

            # Buscar el usuario por nombre de usuario
            user = collection.find_one({"username": username})
            if not user:
                raise UserNotFoundError()

            # Validar usuario activo
            if not user["status"]:
                raise UserInactiveError()

            # Verificar la contraseña
            if not UserController.__verification_password(user["password_hash"], password):
                raise IncorrectPasswordError()

            return True
        finally:
            connection.close_connection()

    @staticmethod
    def __hash_password(password: str) -> str:
        # Genera un salt
        salt = bcrypt.gensalt()
        # Hashea la contraseña
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    @staticmethod
    def __verification_password(stored_hash: str, password: str) -> bool:
        # Verifica si la contraseña coincide con el hash almacenado
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
