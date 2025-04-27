import pymysql


class Db:

    def __init__(self):
        self._connection = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            db="oop"

        )


test = Db()
