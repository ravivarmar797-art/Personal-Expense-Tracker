import json

running = True
def save_to_file(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
def load_from_file():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def show_expenses_with_index(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    print("\nIndex  Date         Item                 Category        Amount")
    print("-" * 70)

    for i, expense in enumerate(expenses):
        print(
            f"{i:<6} "
            f"{expense['date']:<12} "
            f"{expense['item']:<20} "
            f"{expense['category']:<15} "
            f"{expense['amount']:>7.2f}"
        )

expenses = load_from_file()
while running:
    print("\n------personal expense tracker-------")
    print("1.add expenses")
    print("2.view expenses")
    print("3.view by caterogy")
    print("4.show the total")
    print("5.Exit")
    print("6.edit expense")
    print("7. delete expense")
    choice = input("Enter the choice(1-7)")
    if choice == "1":
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        while True:
            item = input("Enter item name: ").strip()
            if item:
                break
            else:
                print("Item name cannot be empty.")

        while True:
            category = input("Enter category: ").strip()
            if category:
                break
            else:
                print("Category cannot be empty.")
        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            if len(date) == 10 and date[4] == "-" and date[7] == "-":
                break
            else:
                print("Date must be in YYYY-MM-DD format.")

        expense = {
            "item": item,
            "amount":amount,
            "category":category,
            "date":date
        }
        expenses.append(expense)  
        save_to_file(expenses)
        print("Expense added successfully!")
    elif choice == "2":
        if not expenses:
            print("no expenses recorded yet.")
        else:
            print("\nDate    item    category   amount")
            print("-" * 60)
            for expense in expenses:
                print(
                    f"{expense['date']:<12} "
                    f"{expense['item']:<20} "
                    f"{expense['category']:<15} "
                    f"{expense['amount']:>7.2f}"
                )
    elif choice == "3":
        category_filter = input("Enter category to filter: ")
        found = False
        print("\nDate     item        category           amount")
        print("-" * 60)
        for expense in expenses:
            if expense["category"].lower() == category_filter.lower():
                found = True
                print(
                        f"{expense['date']:<12} "
                        f"{expense['item']:<20} "
                        f"{expense['category']:<15} "
                        f"{expense['amount']:>7.2f}"
                    )
        if not found:
            print("no expenses for this category.")
        
    elif choice == "4":
        if not expenses:
            print("no expenses record yet.")
        else:
            total = 0
            category_totals = {}
            for expense in expenses:
                amount = expense["amount"]
                category = expense["category"]

                total += amount
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
            
        print(f"\ntotal spending: {total:.2f}\n")
        print("category breakdown:")
        print("_" * 25)
    
        for category, amount in category_totals.items():
            print(f"{category:<15} {amount:>8.2F}")
    
    

    elif choice == "5":
        save_to_file(expenses)
        print("Exiting program")
        running = False
    
    elif choice == "6":
        show_expenses_with_index(expenses)

        if not expenses:
            continue
        try:
            index = int(input("Enter index of expense to edit: "))
            if index < 0 or index >= len(expenses):
                print("Invalid index.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        expense = expenses[index]
        print("Press Enter to keep old value")
        new_item = input(f"New item ({expense['item']}): ").strip()
        if new_item:
            expense["item"] = new_item
        while True:
            new_amount = input(f"New amount ({expense['amount']}): ").strip()
            if not new_amount:
                break
            try:
                new_amount = float(new_amount)
                if new_amount > 0:
                    expense["amount"] = new_amount
                    break
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Enter a valid number.")
        new_category = input(f"New category ({expense['category']}): ").strip()
        if new_category:
            expense["category"] = new_category
        new_date = input(f"New date ({expense['date']}): ").strip()
        if new_date:
            expense["date"] = new_date
        save_to_file(expenses)
        print("Expense updated successfully!")

    elif choice == "7":
        show_expenses_with_index(expenses)

        if not expenses:
            continue

        try:
            index = int(input("Enter index to delete: "))
            if index < 0 or index >= len(expenses):
                print("Invalid index.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        confirm = input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            del expenses[index]
            save_to_file(expenses)
            print("Expense deleted successfully!")
        else:
            print("Delete cancelled.")
   


