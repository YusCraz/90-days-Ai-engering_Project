expenses = [
    {"name": "Chipotle", "category": "Food", "amount": 14.50},
    {"name": "Gas", "category": "Transportation", "amount": 42.30},
    {"name": "Coffee", "category": "Food", "amount": 5.75},
    {"name": "Textbook", "category": "School", "amount": 89.99},
    {"name": "Gym", "category": "Fitness", "amount": 25.00},
]


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return total
    
    
    
    
    
    
def calculate_average(expenses):
    expenses_sum = calculate_total(expenses)
    avg = expenses_sum / len(expenses)
    return avg
    
    




def find_largest_expense(expenses):
    largest = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] > largest["amount"]:
            largest = expense
        
    return largest
    
    
    
    
    
def main():
  
   print(f"Total spent; {calculate_total(expenses):.2f}")
   
   print(f"Average expense: {calculate_average(expenses):.2f}")
   larges = find_largest_expense(expenses)
   
   print(f" Largest expense : {larges['name']  } - ${larges['amount']:.2f}")
   
   
   
main()
