from xml.dom import VALIDATION_ERR
from Models.Db import Db

class Car(Db):
    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004, "rented": True,"rented_until": "30.05.2025"},
            {"model": "A5", "production_year": 2003, "rented": False, "rented_until": None},
            {"model": "A6", "production_year": 2005, "rented": False, "rented_until": None}
        ],
        "BMW": [
            {"model": "M5", "production_year": 2011, "rented": True , "rented_until": "12.12.2025"},
            {"model": "M3", "production_year": 2010, "rented": False,"rented_until": None}
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015, "rented": True,"rented_until": "30.07.2025"},
            {"model": "GLE", "production_year": 2016, "rented": False,"rented_until": None}
        ]
    }

    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None
        self.__rented = None
        self.__rented_until = None
        super().__init__()

        self.__rented_until = None
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("brand musst be set")
        # isto bi bilo valid_models=[car["model"] for car in Car.Valid_cars[self.__brand]]
        valid_models = []
        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car["model"])

        self.__model = model

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model["model"] == model:
                print(car_model["production_year"])

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid car")
        self.__brand = brand

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):

        if self.__model is None:
            raise ValueError("Production year cannot be set")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set")

        self.__production_year = year





audi = Car()

