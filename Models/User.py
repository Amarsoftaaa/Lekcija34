from Models.Db import Db

class User(Db):

    def __init__(self):
        super().__init__()
        print(self._connection)

    def get_age(self,age):
        return self.__age

    def set_age(self,age):
        if age < 18 :
            raise ValueError("Korisnik nije punoljetan")
        self.__age=age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if len(name) < 5:
            raise ValueError("Ime mora imati najmanje 5 znakova")
        self.__name=name

