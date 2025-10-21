import os
import csv

expenses = []

def create_monthly_budget():
    return float(input("Enter the monthly Budget for the month: "))

def calculate_monthly_expenses():
    global expenses
    monthly_budget = create_monthly_budget()

    calculated_budget = 0
    for row in expenses:
        if not row["Amount"]:
            continue
        calculated_budget += float(row["Amount"])
    
    if calculated_budget > monthly_budget:
        print("^" * 70)
        print(f"[INFO] Over budget by ₹{calculated_budget - monthly_budget:.2f}")
    else:
        print("!" * 70)
        print(f"[INFO] You have ₹{monthly_budget - calculated_budget:.2f} left in your budget.")
    
def load_expenses_from_file():
    filename = "expenses_saved.csv"
    global expenses

    if not os.path.isfile(filename):
        return expenses
    
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    return expenses

def enter_expenses_details():
    #Get the details of the user
    global expenses
    print("=" * 70)
    date = input("Enter the date of expense (YYYY-MM-DD): ").strip()
    category = input("Enter the category (e.g, Food, Travel, Health, etc): ").strip()
    while True:
        try:
            amount = float(input("Enter the amount spent: ").strip())
            break
        except ValueError:
            print("Invalid input: Please enter a valid number for the amount.")

    description = input("Enter a brief description of the expense: ").strip()

    expense = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

    expenses.append(expense)
    print("\nExpenses added")

def save_expenses_to_file():
    global expenses
    filename = "expenses_saved.csv"
    file_exists = os.path.isfile(filename)
    # write_header = True
    # if file_exists and os.path.getsize(filename) > 0:
    #     write_header = False

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount", "Description"])
        # if write_header:
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)


def display_the_expenses():
    global expenses

    if not expenses:
        print("\nNo expense  found.")
        return
    
    print("#" * 70)
    print(f"{'All Recorded Expenses':>45}")
    print("#" * 70)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 70)

    missing_records = []
    for row in expenses:
        missing_fields = [key for key,value in row.items() if value is None or  str(value).strip()  == '']
        if missing_fields:
            missing_records.append(row)
        else:
            print(f"{row['Date']:<12} | {row['Category']:<15} | {row['Amount']:<10} | {row['Description']}")
    
    if missing_records:
        print("*" * 70)
        print(f"{'Missing Records':>45}")
        print("*" * 70)
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
        print("-" * 70)
        for items in missing_records:
            print(f"{items['Date']:<12} | {items['Category']:<15} | {items['Amount']:<10} | {items['Description']}")

    print("#" * 70)
    print(f"[INFO] Total no. of records: {len(expenses)}")
    print(f"[INFO] Records with missing fields: {len(missing_records)}")

def user_menu():
    while True:
        print("\n"+"+"*70)
        print(f"{'Personal Expense Tracker':>45}")
        print("+"*70)
        print("1. Add New Expenses")
        print("2. View All Expenses")
        print("3. Track montly budget")
        print("4. Save Expenses to a file")
        print("5. Exit")
        print("="*70)

        choice = input("Enter the choice(1-5): ")

        if choice == '1':
            enter_expenses_details()
        elif choice == '2':
            display_the_expenses()
        elif choice == '3':
            calculate_monthly_expenses()
        elif choice == '4':
            save_expenses_to_file()
        elif choice == '5':
            print("\n Thanks for using Personal Expense tracker, Goodbye!!!")
            break
        else:
            print("Invalid choice, please select a choice (1-5).")

if __name__=="__main__":
    load_expenses_from_file()
    user_menu()
            
