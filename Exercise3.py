name = "Erin Sophia V. Estrella"
Act = "\nExercise 3 - Create simple ATM with loop"
Sec = "BSIS 3A-G2"

print(name)
print(Sec)
print(Act)

print("\n=== BeepBoop ATM ===")

balance = 1000   # starting balance

while True:
    print("\nChoose an option:")
    print("1 - Check Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")

    choice = input("\nEnter your choice: ")

    # CHECK BALANCE
    if choice == "1":
        print("\nYour current balance is:", balance)

    # DEPOSIT
    elif choice == "2":
        deposit_amount = float(input("\nEnter amount to deposit: "))
        balance = balance + deposit_amount
        print("Deposit successful!")
        print("\nNew balance:", balance)

    # WITHDRAW
    elif choice == "3":
        withdraw_amount = float(input("\nEnter amount to withdraw: "))

        while withdraw_amount > balance:
            print("\nYou have entered more than your balance amount, Try again")
            withdraw_amount = float(input("Enter amount to withdraw: "))

        balance = balance - withdraw_amount
        print("Withdrawal successful!")
        print("\nRemaining balance:", balance)

    # EXIT
    elif choice == "4":
        print("Thank you for using the BeepBoop ATM!")
        break

    # INVALID
    else:
        print("Invalid choice. Please select 1-4.")