class Student:
    def __init__(self, name, surname, student_id, address, phone_number, email, class_level):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.class_level = class_level

class StudentManagement:
    def __init__(self):
        self.students = []
        # Initialisation de la liste des étudiants

    def add_student(self, student):
        self.students.append(student)
        # Ajouter un nouvel étudiant à la liste

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                 # Supprimer un étudiant en fonction de son id
                print(f"Student with ID {student_id} successfully removed.")
                return
        print(f"No student found with ID {student_id}.")

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.show_student_details(student)
                return
                # Afficher les détails d'un étudiant en fonction de son id
        print(f"No student found with ID {student_id}.")

    def modify_student(self, student_id, **kwargs):
        for student in self.students:
            if student.student_id == student_id:
                for key, value in kwargs.items():
                    setattr(student, key, value)
                    # Modifier les détails d'un étudiant en fonction de son id
                print(f"Student details with ID {student_id} modified successfully.")
                return
        print(f"No student found with ID {student_id}.")

    def show_student_details(self, student):
        print(f"Name: {student.name}, Surname: {student.surname}, Student ID: {student.student_id}, Address: {student.address}, Phone Number: {student.phone_number}, Email: {student.email}, Class Level: {student.class_level}")

def main_menu():
    print("\nMain Menu:")
    print("1. Add a new student")
    print("2. Display list of all students")
    print("3. Search for a student by ID")
    print("4. Modify student details")
    print("5. Remove a student")
    print("6. Quit")

def input_student_details():
    name = input("Enter student's name: ")
    surname = input("Enter student's surname: ")
    student_id = input("Enter student's ID: ")
    address = input("Enter student's address: ")
    phone_number = input("Enter student's phone number: ")
    email = input("Enter student's email: ")
    class_level = input("Enter student's class level: ")
    return Student(name, surname, student_id, address, phone_number, email, class_level)

if __name__ == "__main__":
    student_management = StudentManagement()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdd a new student:")
            student = input_student_details()
            student_management.add_student(student)
            print("Student added successfully.")

        elif choice == "2":
            print("\nList of all registered students:")
            for student in student_management.students:
                student_management.show_student_details(student)

        elif choice == "3":
            student_id = input("\nEnter the student ID to search for: ")
            student_management.search_student_by_id(student_id)

        elif choice == "4":
            student_id = input("\nEnter the student ID to modify: ")
            field = input("Enter the field to modify (name, surname, student_id, address, phone_number, email, class_level): ")
            new_value = input(f"Enter the new value for {field}: ")
            student_management.modify_student(student_id, **{field: new_value})

        elif choice == "5":
            student_id = input("\nEnter the student ID to remove: ")
            student_management.remove_student(student_id)

        elif choice == "6":
            print("The student management system is finished")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
