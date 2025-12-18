import math

class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount*-1, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance=0
        for item in self.ledger:
            balance+=item['amount']
        return balance

    def transfer(self, amount, another_category):
        if self.withdraw(amount, f"Transfer to {another_category.name}"):
            another_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        else:
            return False


    def __str__(self):
        rows=''
        for item in self.ledger:
            rows+=f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"

        return(f'{math.ceil((30-len(self.name))/2)*"*"}{self.name}{(30-len(self.name))//2*"*"}\n{rows}Total:{self.get_balance():>7.2f}')


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


def create_spend_chart(categories):
    total_spends=[]
    for category in categories:
        category_spends=0
        for record in category.ledger :
            if record['amount']<0:
                category_spends+=abs(record['amount'])
        total_spends.append(category_spends)
    return(f"Percentage spent by category\n")

print(create_spend_chart(''))