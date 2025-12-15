import util as u
students = u.load_data()
print("Welcome to the Students Enrollment system")
while True:
    option = u.show_menu()
    match option:
        case 1:
            u.add_student(students)
        case 2:
            u.search_student(students)
        case 3:
            u.edit_student(students)
        case 4:
            u.remove_student(students)
        case 5:
            u.print_student(students)
        case 6:
            u.save_data(students)
    continue_option = str(input("What you like to continue(y/yes), or exit the program(n/no)?\n")).lower()
    if continue_option == "n" or continue_option == "no":
        break
    
