"""
Logic:

expenses.txt
    ↓
load expenses
    ↓
show/calculate expenses
    ↓
calculate total
    ↓
calculate average
    ↓
find most expensive
    ↓
allow user to add expense
    ↓
save updated expenses.txt
"""

from pathlib import Path


# ---------- FILE PATH ----------

file = Path(__file__)
folder = file.parent / "expenses.txt"


# ---------- LOAD EXPENSES ----------

def load_expenses():
    read = folder.read_text()
    expenses = read.splitlines()

    return expenses


# ---------- CALCULATE TOTAL ----------

def total_expenses(expenses):
    total = 0

    for expense in expenses:
        parts = expense.split(",")
        price = float(parts[1])
        total += price

    return total


# ---------- CALCULATE AVERAGE ----------

def calculate_avg(expenses):
    total = total_expenses(expenses)
    avg = total / len(expenses)

    return avg


# ---------- FIND MOST EXPENSIVE ----------

def most_expensive(expenses):
    most_expensive = expenses[0]

    parts = most_expensive.split(",")
    highest_price = float(parts[1])

    for expense in expenses[1:]:
        parts = expense.split(",")
        price = float(parts[1])

        if price > highest_price:
            highest_price = price
            most_expensive = expense

    return most_expensive


# ---------- ADD NEW EXPENSE ----------

def add_expense(expenses):
    new_item = input("Enter the item you bought: ")
    new_price = input(f"Enter the price of your {new_item}: ")

    new_expense = f"{new_item},{new_price}"

    expenses.append(new_expense)

    return expenses


# ---------- SAVE UPDATED EXPENSES ----------

def save_expenses(expenses):
    text = "\n".join(expenses)
    folder.write_text(text)


# ---------- SHOW ALL EXPENSES ----------

def show_expenses(expenses):
    for expense in expenses:
        print(expense)


# ---------- MAIN ----------

def main():
    expenses = load_expenses()

    print(f"Your Total is: ${total_expenses(expenses):.2f}")
    print(f"Your Average is: ${calculate_avg(expenses):.2f}")
    print(f"Your Most Expensive is: {most_expensive(expenses)}")

    add_expense(expenses)
    save_expenses(expenses)

    print("\nUpdated Expenses:")
    show_expenses(expenses)


if __name__ == "__main__":
    main()