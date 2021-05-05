class User:
    bank_name = "WatUp Bank"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(self.account_balance)
        return self
    def display_user_balance(self):
        print("Your balance is:")
        print(self.account_balance)
        return self

jimbo = User("Jimbo Scruggs", "jimbo@email.com")
al = User("Al Simmons", "alspals@email.com")
tom = User("Tom Flom", "tommyboyy@email.com")

print(jimbo.name)
jimbo.display_user_balance()
jimbo.make_deposit(200)
jimbo.make_deposit(100)
jimbo.make_deposit(120)
jimbo.make_withdrawal(50)
jimbo.display_user_balance()

print(al.name)
al.display_user_balance()
al.make_deposit(120)
al.make_deposit(120)
al.make_withdrawal(50)
al.make_withdrawal(70)
al.display_user_balance
al.display_user_balance()

print(tom.name)
tom.display_user_balance()
tom.make_deposit(80)
tom.make_withdrawal(50)
tom.make_withdrawal(90)
tom.make_withdrawal(120)
tom.display_user_balance()