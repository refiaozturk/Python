employees = []

def add_employee():
    name = input("Enter employee's name: ").title()
    salary = input("Enter employee's salary: ")

    if salary.isdigit():
        employees.append({"name": name, "salary": int(salary)})
        print(f"Employee named {name} has been added.")

    else:
        print("You entered an invalid salary. Please try again.")


def list_employess():
    if not employees:
        print("No employees have been added yet.")

    else:
        for employee in employees:
            print(f"Employee: {employee['name']}, Salary: {employee['salary']}")


def filter_employees_by_salary(min_salary):
    filtered_employees = list(filter(lambda employee: employee['salary'] > min_salary, employees))

    if not filtered_employees:
        print(f"There is no employee with a salary higher than {min_salary}.")
    
    else:
        for employee in filtered_employees:
            print(f"Employee: {employee['name']}, Salary: {employee['salary']}")


def main():
    while True:
        print("""
              Employee Salary Management System
              ----------------------------
              1. Add Employee
              2. List Employees
              3. Filter Out Employees with a Specific Salary Higher
              4. Exit
              """)
        
        choice = input("Please make your selection from the list provided (1-4): ")

        if choice == "1":
            add_employee()
        
        elif choice == "2":
            list_employess()

        elif choice == "3":
            min_salary = input("Enter the minimum salary value: ")

            if min_salary.isdigit():
                filter_employees_by_salary(int(min_salary))

            else:
                print("You entered an invalid salary. Please try again.")

        elif choice == "4":
            print("The program is shutting down...")
            print("The program has been shut down.")
            break

        else:
            print("You made an invalid selection. Please try again.")

if __name__ == "__main__":
    main()