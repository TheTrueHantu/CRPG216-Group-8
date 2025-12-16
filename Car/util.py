import CarClass as Car
def show_menu():
    print("What would you like to do today?")
    print("-Add a car? enter 1")
    print("-Search for car? enter 2")
    print("-Edit car info? enter 3")
    print("-Remove a car? enter 4")
    print("-Print the car list? enter 5")
    print("-Save the data to a file? enter 6")
    print('-Exit? enter 0')
    option = int(input("\n"))
    return option

def add_car(cars):
    option = "y"
    while option == "y" or option == "yes":
        print("Enter id of the car, followed by the car's information.")
        id = int(input("Id:\n"))
        name = input("name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = int(input("year:\n"))
        value = int(input("value:\n"))
        id_exists = False
        name_exist = False
        for c in cars:
            if c.car_id == id:
                id_exists = True
                break
            elif c.name == name:
                name_exist = True
                break
        if id_exists:
            print("Incorrect Id. Id already exist in the system")
        elif name_exist:
            print("The car is already in the inventory. No action is required..")
        else:
            car = Car.Car(id, name, make, body, year, value)
            cars.append(car)
 
            print("car is added to the inventory.")
            print(car)
 
        option = str(input("Do you want to add more cars? y(yes)/n(no)\n")).lower()

def remove_car(cars):
    option = "y"
    while option == "y" or option == "yes":
        print("Enter id of the car that you want to remove from the inventory.")
        id = int(input("id:\n"))
        removed = False
 
        for c in cars:
            if c.car_id == id:
                cars.remove(c)
                removed = True
                print("car removed")
                break
              
 
        if not removed:
            print("car not found")
 
        option = input("Do you want to remove more cars? y(yes)/n(no)\n").lower()

def load_data():
    cars = []
    reader = open("data.txt", "r")
    for line in reader:
        line = line.strip()
        seperate = line.split(",")
        id = int(seperate[0])
        name = str(seperate[1])
        make = str(seperate[2])
        body = str(seperate[3])
        year = int(seperate[4]) 
        value = int(seperate[5])
        car = Car.Car(id,name,make,body,year,value)
        cars.append(car)
    reader.close()

    return cars

def search_car(cars):
    while True:
        user_option = int(input("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu\n"))
        found = False
        if user_option == -1:
            break
        elif user_option == 1:
            id_search_input = int(input("Please Enter the id of the car:\n"))
            for c in cars:
                if c.car_id == id_search_input:
                    print("Car found ", c)
                    found = True
                    break 
            if not found:
                print("Car not found")
        elif user_option == 2:
            name_input = str(input("Please Enter the name of the car:\n"))
            for c in cars:
                if c.name.lower() == name_input.lower():
                    print("Car found ", c)
                    found = True
                    break
            if not found:
                print("Car not found")

def edit_cars(cars):
    while True:
        id_input = int(input("Enter the id of the car. Enter -1 to return to the previous menu\n"))
        if id_input == -1:
            break
        car = None
        for c in cars:
            if c.car_id == id_input:
                car = c
                break
        if car == None:
            print("Student not found")
        else:
            name = str(input("Name:\n"))
            make = str(input("make:\n"))
            body = str(input("Body:\n"))
            year = int(input("year:\n"))
            value = int(input("value:\n"))

            car.name = name
            car.make = make
            car.body = body
            car.year = year
            car.value = value

            print("Car's new info is", car)
            
def print_cars(cars):
    for c in cars:
        print(c)

def save_data(cars):
    writer = open("data.txt", "w")
    for c in cars:
        line = f"{c.car_id},{c.name},{c.make},{c.body},{c.year},{c.value}\n"
        writer.write(line)
    writer.close()
    print("Data saved to local file successfully!")