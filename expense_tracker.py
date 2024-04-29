from expenses import Expense
import calendar
import datetime


def main():
    print(f"Welcome to the Expense Tracker!")
    expense_file_path= "expenses.cvs"
    expenses=get_user_expense()
  
    save_expense_to_file(expenses, expense_file_path)

    summarize_expenses(expense_file_path)
 

def get_user_expense():
    print(f"Enter your expense details:")
    expense_name = input("enter expense name")
    expense_amount = float(input("enter expense amount"))
    expense_categories=["food","home","work","fun","misc"]


    while True:
      print("Select category:")
      for i,category_name in enumerate(expense_categories):
        print(f"{i+1}. {category_name}")

      value_range = f"[1- {len(expense_categories)}]"
      selected_index=int(input(f"enter the category value {value_range}:")) -1
      if selected_index in range(len(expense_categories)):
          selected_category= expense_categories[selected_index]
          new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
          return new_expense
      else:
        print("invalid category value,please try again!")
          
def save_expense_to_file(expenses: Expense, expense_file_path):
    print(f"Expense details saved: {expenses} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
      f.write(f"{expenses.name},{expenses.category},{expenses.amount}\n")
    

def summarize_expenses(expense_file_path,budget):
    print(f"Expenses summarized.")
    with open(expense_file_path, "r") as f:
      lines=f.readlines()
      for line in lines:
          expense_name,expense_category,expense_amount= line.strip().split(",")
          line_expense= Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
          expenses.append(line_expense)
    amount_by_category = {}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
          amount_by_category[key] += expense.amount
        else:
          amount_by_category[key] = expense.amount
    print("expenses by category")      
    for key,amount in amount_by_category.items():
      print(f"  {key}:  ${amount:.2f}")

    total_spent =sum([x.amount for x in expenses])
    print(f"total spent: ${total_spent:.2f}")

    remaning_budget = budget-total_spent
    print(f"remaining budget: ${remaning_budget:.2f}")  

    now =datetime.datetime.now()
    day_in_month= celender.monthrange(now.year,now.month)[1]
    remaning_days= day_in_month-now.day
  

    daily_budget= remaning_budget/remaning_days
    print(f"daily budget: ${daily_budget:.2f}")

  
    print(amount_by_category)
if __name__ == "__main__":
  main()