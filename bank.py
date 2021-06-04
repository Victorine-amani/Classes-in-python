class Account:
    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.transaction_fee=300
        self.loan_limit=10000
        self.loan=0
        self.loan_fees=0.05
        
        

    def deposit(self,amount):
        
        if amount<=0:
            return f'Please deposit a valid amount'
        else:
            self.balance +=amount
            return f'Hello {self.name} you have deposited {amount} your new balance is {self.balance}'

    def withdraw(self,amount):
        transaction=amount+amount*0.05
        if amount<=0:
            return f'Invalid input'

        elif self.balance<=transaction:
            return f'Insufficient balance'

        else:
             
            self.balance-=transaction
            return f'Transaction successful you have withdrawn {amount} your balance is {self.balance}'

    def borrow(self,amount):
        
        total_loan=amount+amount*self.loan_fees
        if amount<=0:
            return f'Invalid input'
        elif total_loan >self.loan_limit:
            return f'{amount} is greater than limit try a lower amount'
        elif self.loan>0:
            return f'Repay your outstanding loan of {self.loan}'
        else:
            loan=self.balance+amount
            self.loan+=total_loan
            return f'You new balance is {loan}. Repay {total_loan} in 30 days'
