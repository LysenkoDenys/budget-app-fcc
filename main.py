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

#=================================
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

#=================================
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")

clothing = Category("Clothing")
clothing.deposit(500, "deposit")
clothing.withdraw(50, "shirt")
clothing.withdraw(25, "pants")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(100, "fuel")

categories = [food, clothing, auto]
#=================================

def create_spend_chart(categories):
    total_spends=[]
    for category in categories:
        category_spends=0
        for record in category.ledger :
            if record['amount']<0:
                category_spends+=abs(record['amount'])
        total_spends.append(category_spends)
    total_spends_sum=sum(total_spends)
    percentages=[]
    for category_item in total_spends:
        percentages.append(int((category_item / total_spends_sum * 100) // 10) * 10)
    scale_y=''  
    for line in range(100,-1,-10):
        scale_y+=f"{line:>3}|"
        for p in percentages:
            if p>=line:
                scale_y+=' o '
            else:
                scale_y+='   '
        scale_y+=' \n'

    max_length_of_word=max(len(w.name) for w in categories)
    horizontal_line='    ' + '---' * len(categories) + '-\n'
    
    scale_x=''
    for n in range(max_length_of_word):
        line='    '
        for category in categories:
            if n < len(category.name):
                line+=f" {category.name[n]} "
            else:
                line += "   "
        scale_x += line
        if n != max_length_of_word - 1:
            scale_x += "\n"

    for line in scale_x.split("\n"):
        print(len(line), repr(line))

    scale_x = scale_x.rstrip('\n')
    return f"Percentage spent by category\n{scale_y}{horizontal_line}\n{scale_x}"

print(create_spend_chart(categories))