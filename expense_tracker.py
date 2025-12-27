expenses = []
running = True
while running:
    print("\n------personal expense tracker-------")
    print("1.add expenses")
    print("2.view expenses")
    print("3.view by caterogy")
    print("4.show the total")
    print("5.Exit")
    choice = input("Enter the choice(1-5)")
    if choice == "1":
        item = input("Enter item name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        expense = {
            "item": item,
            "amount":amount,
            "category":category,
            "date":date
        } 
        expenses.append(expense)
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
        print("Exiting program")
        running = False
    
    else:
        print("invalid choice. pls enter 1 to 5.")


