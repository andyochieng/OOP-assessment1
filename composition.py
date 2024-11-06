# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for a general employee.")

# Subclass
class Manager(Employee):
    def calculate_salary(self):
        base_salary = 50000
        bonus = 15000
        total_salary = base_salary + bonus
        print(f"Manager's salary: Ksh{total_salary}")

employee = Employee()
employee.calculate_salary()
manager = Manager()
manager.calculate_salary()
