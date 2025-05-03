from datetime import datetime

from Models.Car import Car
from Models.Db import Db


class InsertCar(Db):
    def __init__(self):
        super().__init__()

    def insert_car(self):
        cursor = self._connection.cursor()

        for brands, cars in Car.VALID_CARS.items():
            for car in cars:
                model = car["model"]
                year = car["production_year"]
                rented = car["rented"]
                rented_until = car["rented_until"]

                if rented_until:
                    rented_until = datetime.strptime(rented_until, "%d.%m.%Y").strftime("%Y-%m-%d")
                else:
                    rented_until = None

                print(f"Inserting: {brands}, {model}, {year}, {rented}, {rented_until}")
                cursor.execute("INSERT INTO cars (car_brands,cars_model,cars_year,rented,rented_until)"
                               "VALUES (%s,%s,%s,%s,%s)", (brands, model, year, rented, rented_until))

        self._connection.commit()
        cursor.close()


if __name__ == "__main__":
    try:
        inserter = InsertCar()
        inserter.insert_car()
        print("Cars successfully inserted into database!")
    except Exception as e:
        print(f"Error: {e}")
