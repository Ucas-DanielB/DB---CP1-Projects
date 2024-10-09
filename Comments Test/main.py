 #The bank account function takes the self account number and sets it to the account number, self balance is set to balance, which is 0.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

#Makes an if statement to deposit, and if amount is greater than 0, self balance will increase amount, and return true or false.
    def deposit(self, amount): 
        if amount > 0:
            self.balance += amount
            return True
        return False

#Makes an if statement to withdraw, if 0 is less than amount, and is amount is less than or equal to balance, then self balance subtracts the amount.
    def withdraw(self, amount): 
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

#Makes a function to get_balance with self as a parameter, and will return self balance.
    def get_balance(self): 
        return self.balance

#Makes a function to create an account, that asks for the user unput, and converts the input into a decimal(float), and then returns the bank account with account number and initial balance.
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

#Creates a function for main, when account are true, it prints create account, deposit, withdraw, check balance, and exit.
def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        #Makes an if statements, which makes the choice variable equal to 1, account is set to create_account, accounts is set to account, and prints the success of the account and number.
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        #Creates an elif, which then has variable choice check if the value exists in th list, then makes an input for the user.
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            #Makes an if, which has account_number check value in accounts, then sets account to accounts.
            if account_number in accounts:
                account = accounts[account_number]
                #makes an if, which has choice equal to 2, and asks for an input in the amount variable, which also sets the input into a float.
                if choice == '2': 
                    amount = float(input("Enter deposit amount: "))
                    #Makes an if, which has account deposit the amount, and prints out the success of it.
                    if account.deposit(amount): 
                        print(f"Deposited ${amount:.2f} successfully!")
                        #Makes an else, which will print the invalid deposit amount.
                    else:
                        print("Invalid deposit amount.")
                #Makes an elif, which equals choice to 3, asks for input in the amount variable, and also sets the input to a float.
                elif choice == '3': 
                    amount = float(input("Enter withdrawal amount: "))
                    #Makes an if which the account wants to withdraw from amount, and will print the success.
                    if account.withdraw(amount): 
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    #Makes an else which will print invalid.
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                #Makes an else which will print current balance.
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            #Makes an else which prints that the account was not found.
            else:
                print("Account not found.")
        
        #Makes an elif which equals choice to 5, and prints a thank you and goodbye.
        elif choice == '5': 
            print("Thank you for using our banking system. Goodbye!")
            break
        
        #Makes an else which prints something went wrong.
        else:
            print("Invalid choice. Please try again.")

#Makes an if, which if __name__ equals to "__main__".
if __name__ == "__main__": 
    main()