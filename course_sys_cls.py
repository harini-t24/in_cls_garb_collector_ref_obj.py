import gc
import sys

class Student:
    student_count = 0

    class Course:
        def __init__(self, course_id, course_name):
            self.course_id = course_id
            self.course_name = course_name

        def display_course(self):
            print("Course ID :", self.course_id)
            print("Course Name :", self.course_name)

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.courses = []
        Student.student_count += 1
        print(f"\nStudent {self.name} registered successfully!")

    def add_course(self, course_id, course_name):
        course = Student.Course(course_id, course_name)
        self.courses.append(course)

        # Reference count
        print(f"Reference Count of {course.course_name}:",
              sys.getrefcount(course) - 1)

    def display_student(self):
        print("\n--- Student Details ---")
        print("Roll No :", self.roll_no)
        print("Name :", self.name)
        print("Enrolled Courses:")
        for c in self.courses:
            c.display_course()
            print()

    def __del__(self):
        print(f"Student {self.name} object deleted.")
        Student.student_count -= 1


# Main Program
students = []

while True:
    print("\n===== MENU =====")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")

        stu = Student(roll_no, name)

        n = int(input("How many courses to add: "))
        for i in range(n):
            print(f"\nEnter Course {i+1} Details")
            cid = input("Enter Course ID: ")
            cname = input("Enter Course Name: ")
            stu.add_course(cid, cname)

        students.append(stu)

    elif choice == 2:
        if students:
            print("\n===== Student List =====")
            for s in students:
                s.display_student()
            print("Total Students:", Student.student_count)
        else:
            print("No students available.")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

gc.collect()
