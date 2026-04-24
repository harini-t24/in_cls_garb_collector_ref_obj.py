import gc

class Employee:
    employee_count = 0

    class Address:
        def __init__(self, street, city, state, pincode):
            self.street = street
            self.city = city
            self.state = state
            self.pincode = pincode

        def display_address(self):
            print("Street :", self.street)
            print("City :", self.city)
            print("State :", self.state)
            print("Pincode:", self.pincode)

    def __init__(self, emp_id, name, salary, street, city, state, pincode):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.address = Employee.Address(street, city, state, pincode)
        Employee.employee_count += 1
        print(f"\nEmployee {self.name} hired successfully!")

    def display_employee(self):
        print("\n--- Employee Details ---")
        print("ID :", self.emp_id)
        print("Name :", self.name)
        print("Salary :", self.salary)
        self.address.display_address()

    def __del__(self):
        print(f"Employee {self.name} resigned / removed.")
        Employee.employee_count -= 1


# Main Program
employees = []

while True:
    print("\n===== MENU =====")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many employees to add: "))
        for i in range(n):
            print(f"\nEnter details of Employee {i+1}")
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: "))
            street = input("Enter Street: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            pincode = input("Enter Pincode: ")

            emp = Employee(emp_id, name, salary, street, city, state, pincode)
            employees.append(emp)

    elif choice == 2:
        n = int(input("How many employees to remove: "))
        for i in range(n):
            if employees:
                removed_emp = employees.pop()
                del removed_emp
            else:
                print("No employees to remove.")
        gc.collect()

    elif choice == 3:
        if employees:
            print("\n===== Employee List =====")
            for emp in employees:
                emp.display_employee()
            print("\nTotal Employees:", Employee.employee_count)
        else:
            print("No employees available.")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
