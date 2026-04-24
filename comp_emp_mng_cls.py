import sys
import gc

class Company:
    def __init__(self, cname):
        self.cname = cname
        self.employees = []

    class Employee:
        def __init__(self, emp_id, emp_name, company):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.company = company

        def display_details(self):
            print("Employee ID :", self.emp_id)
            print("Employee Name :", self.emp_name)
            print("Company Name :", self.company.cname)

        def __del__(self):
            print(f"Employee {self.emp_name} object deleted from memory.")

    def add_employee(self, emp_id, emp_name):
        emp = Company.Employee(emp_id, emp_name, self)
        self.employees.append(emp)
        print(f"\n{emp_name} hired successfully!")

        print("Employee Reference Count :", sys.getrefcount(emp) - 1)
        print("Company Reference Count :", sys.getrefcount(self) - 1)

    def remove_employee(self, emp_id):
        found = False
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"\n{emp.emp_name} resigned successfully!")
                del emp
                gc.collect()
                found = True
                break
        if not found:
            print("Employee ID not found.")

    def display_all(self):
        if self.employees:
            print("\n===== Employee List =====")
            for emp in self.employees:
                emp.display_details()
                print("-------------------")
        else:
            print("\nNo employees available.")


# Main Program
cname = input("Enter Company Name: ")
company = Company(cname)

num_employees = int(input("Enter number of employees to add: "))

for i in range(num_employees):
    print(f"\nEnter Employee {i+1} Details")
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    company.add_employee(emp_id, emp_name)

print("\nEmployees after Hiring:")
company.display_all()

remove_count = int(input("\nEnter number of employees to remove: "))

for i in range(remove_count):
    emp_id = input("Enter Employee ID to remove: ")
    company.remove_employee(emp_id)

print("\nEmployees after Removal:")
company.display_all()

print("\nFinal Garbage Collection Running...")
gc.collect()
