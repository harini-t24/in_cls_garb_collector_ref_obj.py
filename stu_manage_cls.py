import sys
import gc


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []

    # Inner Class
    class Student:
        def __init__(self, rollno, name, university):
            self.rollno = rollno
            self.name = name
            self.university = university

        def display_details(self):
            print("Roll No :", self.rollno)
            print("Name :", self.name)
            print("University :", self.university.university_name)

        def __del__(self):
            print(f"Student object {self.name} deleted from memory")

    # Add multiple students
    def add_student(self):
        n = int(input("How many students to add? : "))
        for i in range(n):
            print(f"\nEnter details of Student {i+1}")
            rollno = int(input("Enter Roll Number: "))
            name = input("Enter Student Name: ")
            s = University.Student(rollno, name, self)
            self.students.append(s)
            print(name, "added successfully")

    # Remove multiple students
    def remove_student(self):
        n = int(input("How many students to remove? : "))
        for i in range(n):
            rollno = int(input("\nEnter Roll Number to remove: "))
            found = False
            for s in self.students:
                if s.rollno == rollno:
                    self.students.remove(s)
                    del s
                    print("Student removed successfully")
                    found = True
                    break
            if not found:
                print("Student not found")

    # Display all students
    def display_all(self):
        if not self.students:
            print("No students available")
        else:
            for s in self.students:
                s.display_details()
                print("-" * 30)


# Main Program
uname = input("Enter University Name: ")
u1 = University(uname)

while True:
    print("\n1. Add Students")
    print("2. Remove Students")
    print("3. Display All Students")
    print("4. Reference Count")
    print("5. Garbage Collection")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        u1.add_student()

    elif choice == 2:
        u1.remove_student()

    elif choice == 3:
        u1.display_all()

    elif choice == 4:
        print("University Reference Count:",
              sys.getrefcount(u1) - 1)

        if u1.students:
            print("First Student Reference Count:",
                  sys.getrefcount(u1.students[0]) - 1)
        else:
            print("No student objects available")

    elif choice == 5:
        print("Running Garbage Collector...")
        gc.collect()

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")

