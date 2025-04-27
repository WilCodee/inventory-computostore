class AuthenticationError(Exception):
    """Excepción base para errores de autenticación."""
    pass


class UserNotFoundError(AuthenticationError):
    """Se lanza cuando el usuario no existe en la base de datos."""

    def __init__(self, message="Usuario no encontrado."):
        super().__init__(message)


class UserInactiveError(AuthenticationError):
    """Se lanza cuando el usuario no está activo."""

    def __init__(self, message="Usuario no activo."):
        super().__init__(message)


class IncorrectPasswordError(AuthenticationError):
    """Se lanza cuando la contraseña es incorrecta."""

    def __init__(self, message="Contraseña incorrecta."):
        super().__init__(message)


class UserAlreadyExistsError(AuthenticationError):
    """Se lanza cuando se intenta crear un usuario que ya existe."""

    def __init__(self, message="El nombre de usuario ya está en uso."):
        super().__init__(message)


class InvalidEmailError(AuthenticationError):
    """Se lanza cuando se intenta crear un usuario con un correo inválido."""

    def __init__(self, message="El correo no es válido."):
        super().__init__(message)
