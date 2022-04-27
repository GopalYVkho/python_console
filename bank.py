class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        return f"Thank You, {self.age} year old, {self.name.title()}"

class Bank(User):
    total_deposits=0
    total_withdraws=0
    def __init__(self,name,age,balance):
        super().__init__(name,age)
        self.balance=balance

    def show_info(self):
        return f"{self.name} has a remaining balance of:{round(self.balance)}"

    def deposite(self):
        dp = float(input(f"{self.name.title()},please enter how mouch You would like to deposit "))
        print("Thank you for depositing...")
        self.balance+=dp
        self.total_deposits+=1
        return f"Your balance is now: {round(self.balance,2)}"
    def withdraw(self):
        wd=float(input(f"{self.name.title()} ,pleace enter how much you would like to withdraw"))
        if self.balance<wd:
            return "You can't Withdraw that Amount"
        else:
            print("Thank You for Withdrawing...")
            self.balance-=wd
            self.total_withdraws+=1
            return f"Your balance is now :{round(self.balance,2)}"


def options(user_two):
    print("Thank You for Creating Your bank account")
    print("Here are a list of otions,please choose the number you want")
    while True:
        option_choice=int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraw\n5) See Total Deposit\n6) Quit\n "))
        if option_choice== 1:
            print(user_one_bank.show_info())
            if option_choice == 1 and user_two!=None:
                print(user_two_bank.show_info())
        elif option_choice == 2:
            print(user_one_bank.withdraw())
            if option_choice ==2 and user_two!=None:
                wd=input(f"{user_two.name} would you like to withdraw? yes or no")
                if wd.lower()=='yes':
                    print(user_two_bank.withdraw())
        elif option_choice == 3:
            print(user_one_bank.deposite())
            if option_choice==3 and user_two!=None:
                dep=input(f"{user_two.name} would you like to deposit? yes or no")
                if dep.lower()=="yes":
                    print(user_two_bank.deposite())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_deposits} withdraw.")
            if option_choice == 4 and user_two!=None:
                print(f"There have been {user_two_bank.total_deposits} withdraw.")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_withdraws} deposit.")
            if option_choice == 5 and user_two!=None:
                print(f"There have been {user_two_bank.total_withdraws} deposit.")
        elif option_choice==6:
            print("Thank you for using BC Bank")
            return False
            break
        else:
            print('pleace choose a number from 1-6.')

def bank_creation(name):
    balance=float(input(f"{name.name.title()}, how much money do you have?"))
    return balance

while True:
    print("Welcome To BC Bank")
    name=input("Enter Your Name ")
    age =int(input("Enter your age "))
    user_one=User(name,age)
    user_two=None
    new_user=input("Would you like to register a new person ? Type 'Yes' to create Your Bank ")
    if new_user.lower()=='yes':
        name = input("Enter the second person's name: ")
        age = int(input("Enter Second person's Age"))
        user_two=User(name,age)
        print("Thank you for registering 2 people.please create your bank account")
        user_one_balance=bank_creation(user_one)
        user_two_balance=bank_creation(user_two)
        user_one_bank=Bank(user_one.name,user_one.age,user_one_balance)
        user_two_bank=Bank(user_two.name,user_two.age,user_two_balance)
        flag=options(user_two)
        if flag == False:
            break
    else:
        user_one_balance=bank_creation(user_one)
        user_one_bank=Bank(user_one.name,user_one.age,user_one_balance)
        flag=options(user_two)
        if flag == False:
            break
