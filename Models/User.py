from Models.Db import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None

    @property
    def age(self, age):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Korisnik nije punoljetan")
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 5:
            raise ValueError("Ime mora imati najmanje 5 znakova")
        self.__name = name
