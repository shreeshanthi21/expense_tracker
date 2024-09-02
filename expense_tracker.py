from expense import Expense

budget = float(input("Enter the budget of the month: "))

def main():
    print("EXPENSE TRACKER")
    expense_file = "expenses.csv"
    
    while True:
        print("\nMENU:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Show summary")
        print("5. Exit")

        choice = int(input("Choose an option (1-5): "))
        
        if choice == 1:
            expense = get_input()
            save_to_file(expense, expense_file)
        elif choice == 2:
            view_expenses(expense_file)
        elif choice == 3:
            delete_expense(expense_file)
        elif choice == 4:
            summary(expense_file, budget)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def get_input():
    print("GETTING USER'S EXPENSES")
    exp_name = input("Enter the expense name: ")
    exp_amt = float(input("Enter the expense amount: "))
    print("You've entered ", exp_name, ": Rs.", exp_amt)
    exp_categories = ["Food", "Home", "Work", "Miscellaneous"]
    while True:
        print("Select a category: ")
        for i in range(0, 4):
            print("  ", i + 1, ".", exp_categories[i])
        selected_number = int(input("Enter the number of the category (1-4): "))
        if 0 < selected_number <= 4:
            selected_cat = exp_categories[selected_number - 1]
            new_expense = Expense(name=exp_name, category=selected_cat, amount=exp_amt)
            return new_expense
        else:
            print("Invalid category chosen, try again!")

def save_to_file(expense: Expense, expense_file):
    print(f"Saving user expense: {expense} to {expense_file}")
    with open(expense_file, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def view_expenses(expense_file):
    print("VIEWING ALL EXPENSES:\n")
    with open(expense_file, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No expenses recorded.")
        else:
            for index, line in enumerate(lines):
                expense_name, expense_category, expense_amount = line.strip().split(",")
                print(f"{index + 1}. {expense_name} | {expense_category} | Rs.{expense_amount}")

def delete_expense(expense_file):
    print("DELETE AN EXPENSE:\n")
    with open(expense_file, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No expenses recorded.")
            return
        
        for index, line in enumerate(lines):
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(f"{index + 1}. {expense_name} | {expense_category} | Rs.{expense_amount}")

        to_delete = int(input("Enter the number of the expense you want to delete: ")) - 1

        if 0 <= to_delete < len(lines):
            del lines[to_delete]
            with open(expense_file, "w") as f:
                f.writelines(lines)
            print("Expense deleted successfully.")
        else:
            print("Invalid selection. Please try again.")

def summary(expense_file, budget_amt):
    print("SUMMARY:\n")
    expenses: list[Expense] = []
    with open(expense_file, "r") as f:
        lines = f.readlines()
        for i in lines:
            expense_name, expense_category, expense_amount = i.strip().split(",")
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    amt_by_cat = {}
    for exp in expenses:
        key = exp.category
        if key in amt_by_cat:
            amt_by_cat[key] += exp.amount
        else:
            amt_by_cat[key] = exp.amount

    for key, amount in amt_by_cat.items():
        print(f"  {key}: Rs.{amount:.2f}")

    total_spent = sum(exp.amount for exp in expenses)
    print(f"You have spent Rs.{total_spent:.2f} this month.")

    remaining = budget_amt - total_spent
    print(f"REMAINING BUDGET: Rs.{remaining:.2f}")

if __name__ == "__main__":
    main()


