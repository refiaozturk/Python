import os

def add_income(income_list):
    income = float(input("Enter the amount of revenue you want to add: "))
    income_list.append(income)

def add_expense(expense_list):
    expense = float(input("Enter the amount of expense you want to add: "))
    expense_list.append(expense)

def show_incomes(income_list):
    print("Income List: ")
    for income in income_list:
        print(f"- {income}")

def show_expenses(expense_list):
    print("Expense List: ")
    for expense in expense_list:
        print(f"- {expense}")

def calculate_budget(income_list, expense_list):
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    budget = total_income - total_expense
    return budget

def save_to_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

def read_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [float(line.strip()) for line in file.readlines()]
    
def main():
    income_list = read_from_file("incomes.txt")
    expense_list = read_from_file("expenses.txt")

    while True:
        print("""
              Personal Finance Management App
              ---------------------------------
              1. Add Income
              2. Add Expense
              3. Show Incomes
              4. Show Expenses
              5. Calculate Monthly Budget
              6. Exit and Save Data
              """)
        
        choice = input("Enter a number (1-6): ")

        if choice == "1":
            add_income(income_list)
        
        elif choice == "2":
            add_expense(expense_list)
        
        elif choice == "3":
            show_incomes(income_list)

        elif choice == "4":
            show_expenses(expense_list)

        elif choice == "5":
            budget = calculate_budget(income_list, expense_list)
            print(f"Your Monthly Budget: {budget}")
        
        elif choice == "6":
            save_to_file("incomes.txt", income_list)
            save_to_file("expenses.txt", expense_list)
            print("The data was recorded. Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()