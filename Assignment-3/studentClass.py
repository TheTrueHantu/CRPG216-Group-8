class Student:
    def __init__(self, id, firstname, lastname, gpa, semester):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gpa = gpa
        self.semester = semester  

    def __str__(self):
        return f"{self.id}\t{self.firstname}\t{self.lastname}\t{self.gpa}\t{self.semester}"