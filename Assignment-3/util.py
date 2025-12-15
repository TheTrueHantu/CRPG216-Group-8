import studentClass as stu
def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    print("-Print the student list? enter 5")
    print("-Save the data to a file? enter 6")
    option = int(input("\n"))
    return option

def add_student(students):
    option = "y"
    while option == "y" or option == "yes":
        print("Enter id of the student, followed by the student's information.")
        id = int(input("Id:\n"))
        first = input("First name:\n")
        last = input("Last name:\n")
        gpa = float(input("GPA:\n"))
        semester = int(input("Semester:\n"))
        id_exists = False
        name_exist = False
        for s in students:
            if s.id == id:
                id_exists = True
                break
            elif s.firstname == first and s.lastname == last:
                name_exist = True
                break
        if id_exists:
            print("Incorrect Id. Id already exist in the system")
        elif name_exist:
            print("The student already enrolled. No action is required..")
        else:
            student = stu.Student(id, first, last, gpa, semester)
            students.append(student)
 
            print("Student Enrolled in the system")
            print(student)
 
        option = str(input("Do you want to add more students? y(yes)/n(no)\n")).lower()

def remove_student(students):
    option = "y"
    while option == "y" or option == "yes":
        print("Enter id of the student that you want to remove from the students' registry.")
        id = int(input("id:\n"))
        removed = False
 
        for s in students:
            if s.id == id:
                students.remove(s)
                removed = True
                print("Student removed")
                break
              
 
        if not removed:
            print("Student not found")
 
        option = input("Do you want to remove more students?y(yes)/n(no)\n").lower()

def load_data():
    students = []
    reader = open("data.txt", "r")
    for line in reader:
        line = line.strip()
        seperate = line.split(",")
        id = int(seperate[0])
        firstName = str(seperate[1])
        lastName = str(seperate[2])
        gpa = float(seperate[3])
        semester = int(seperate[4]) 
        student = stu.Student(id,firstName,lastName,gpa,semester)
        students.append(student)
    reader.close()

    return students

def search_student(students):
    while True:
        user_option = int(input("To search using the Id enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu\n"))
        found = False
        if user_option == -1:
            break
        elif user_option == 1:
            id_search_input = int(input("Please Enter the id of the student:\n"))
            for s in students:
                if s.id == id_search_input:
                    print("Student found ", s)
                    found = True
                    break 
            if not found:
                print("Student not found")
        elif user_option == 2:
            first_name_input = str(input("Please Enter the first name of the student:\n"))
            last_name_input = str(input("Please Enter the last name of the student:\n"))
            for s in students:
                if s.firstname.lower() == first_name_input.lower() and s.lastname.lower() == last_name_input.lower():
                    print("Student found ", s)
                    found = True
                    break
            if not found:
                print("Student not found")

def edit_student(students):
    while True:
        id_input = int(input("Enter the id of the student. Enter -1 to return to the previous menu\n"))
        if id_input == -1:
            break
        student = None
        for s in students:
            if s.id == id_input:
                student = s
                break
        if student == None:
            print("Student not found")
        else:
            firstName = str(input("First name:\n"))
            lastName = str(input("Last name:\n"))
            gpa = float(input("GPA:\n"))
            semester = int(input("Semester:\n"))

            student.firstname = firstName
            student.lastname = lastName
            student.gpa = gpa
            student.semester = semester

            print("Student's new info is ", student)
            
def print_student(students):
    for s in students:
        print(s)

def save_data(students):
    writer = open("data.txt", "w")
    for s in students:
        line = f"{s.id},{s.firstname},{s.lastname},{s.gpa},{s.semester}\n"
        writer.write(line)
    writer.close()
    print("Data saved to local file successfully!")