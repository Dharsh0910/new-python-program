class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = initial_balance
            print("Account created successfully!")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Balance in account {account_number}: ${balance}")
        else:
            print("Account does not exist!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount} deposited successfully into account {account_number}")
            self.check_balance(account_number)
        else:
            print("Account does not exist!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount} withdrawn successfully from account {account_number}")
                self.check_balance(account_number)
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist!")


if __name__ == "__main__":
    atm = ATM()

    while True:
        print("\n1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            atm.create_account(account_number, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            atm.check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(account_number, amount)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
