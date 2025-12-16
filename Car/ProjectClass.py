import util as u
cars = u.load_data()
print("Welcome to the cars inventory system")
while True:
    option = u.show_menu()
    match option:
        case 1:
            u.add_car(cars)
        case 2:
            u.search_car(cars)
        case 3:
            u.edit_cars(cars)
        case 4:
            u.remove_car(cars)
        case 5:
            u.print_cars(cars)
        case 6:
            u.save_data(cars)
        case 0:
            break
