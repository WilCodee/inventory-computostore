from datetime import datetime


class User:
    def __init__(self, username: str, password_hash: str, name: str, email: str, role: str = "admin"):
        self.__username = username
        self.__password_hash = password_hash
        self.__name = name
        self.__email = email
        self.__role = role
        self.__date_creation = datetime.now()
        self.__status = True

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password_hash(self):
        return self.__password_hash

    @password_hash.setter
    def password_hash(self, password_hash: str):
        self.__password_hash = password_hash

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def date_creation(self):
        return self.__date_creation

    @date_creation.setter
    def date_creation(self, date_creation: datetime):
        self.__date_creation = date_creation

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: bool):
        self.__status = status
