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
        print("view expense selected")
    elif choice == "3":
        print("view expense by category selected")
    elif choice == "4":
        print("show the total selected")
    elif choice == "5":
        print("Exiting program")
        running = False
    
    else:
        print("invalid choice. pls enter 1 to 5.")


