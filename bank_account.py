# Bank Account System with Receipt
import time

class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            self.generate_receipt("DEPOSIT", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.generate_receipt("WITHDRAW", amount)
        else:
            print("Insufficient balance!")

    def generate_receipt(self, txn_type, amount):
        print("\n========== RECEIPT ==========")
        print("Transaction Type:", txn_type)
        print("Account Holder:", self.name)
        print("Account No:", self.acc_no)
        print("Amount:", amount)
        print("Balance:", self.balance)
        print("Time:", time.strftime("%d-%m-%Y %H:%M:%S"))
        print("=============================\n")


# Main Program
name = input("Enter your name: ")
acc_no = input("Enter account number: ")
account = BankAccount(name, acc_no, 1000)  # default balance

while True:
    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.show_balance()

    elif choice == "2":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == "3":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice!")
