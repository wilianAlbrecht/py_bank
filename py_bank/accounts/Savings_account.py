from Account import Account

class Savings_account(Account):
    
    def __init__(self, number, agency, balance) -> None:
        super().__init__(number, agency, balance)

    def withdraw(self, withdrawal_amount):
        ...