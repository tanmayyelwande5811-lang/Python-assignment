from bank_package import cust
from bank_package import account

name = input("Enter customer Name: ")
account_no = input("Enter Account Number: ")

cust.display_customer(name, account_no)

while True:
    print("\n----- BANK MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        print("Current Balance:", account.check_balance())
    elif choice == "4":
        print("Thank you for using our banking system")
        break
    else:
        print("Invalid choice")