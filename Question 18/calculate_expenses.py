# calculate_expenses.py

def calculate_total_expenses(file_name):
    total = 0
    with open(file_name, "r") as file:
        for line in file:
            expense = float(line.strip())
            total += expense
    return total

total_expenses = calculate_total_expenses('expenses.txt')
print(f"Total Expenses: ${total_expenses}")
