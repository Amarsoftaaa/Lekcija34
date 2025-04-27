from zoneinfo import available_timezones
from Models.Car import Car
from Models.User import User
#prebaciti svu logiku mysql
#dodati rentiranje automobila (do kada)
#prilikom ispisivanja rentanog auta ispisati pored do kada (npr jos 5 dana)
#ako je manje od 1 dana ispisati u satima (npr 10 sati )

print("Opcije : "
      "\n1. Dodaj korisnika "
      "\n2. Prikazi korisnika "
      "\n3. Prikazi raspoloziva vozila"
      "\n4. Prikazi rentana vozila")

available_options = [1,2,3,4]

option = None

while option is None:

    options = int(input("Unesite opciju koju zelite "))
    print(options)

    if options not in available_options:
        raise ValueError ("Nepoznata opcija")

    if options == 1:
        user = User()
        user.name = input("Enter users name")
        user.age = int(input("Enter users age"))
        user.create()
        option = None

    elif options == 2 :
        print(User.ALL_USERS)
        option = None

    elif options == 3 or options == 4:

        for brand in Car.VALID_CARS:
            for car in Car.VALID_CARS[brand]:
                if not car["rented"] and options == 3:
                    print(car)
                elif car["rented"] and option == 4:
                    print(car)

