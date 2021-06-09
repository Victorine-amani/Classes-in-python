from datetime import datetime

class Account:
    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.transaction_fee=300
        self.loan_limit=10000
        self.loan=0
        self.loan_fees=0.05
        self.transactions=[]
    
    def deposit(self,amount):
        
        if amount<=0:
            return f'Please deposit a valid amount'
        else:
            self.balance +=amount
            transact={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
            self.transactions.append(transact)
            return f'Hello {self.name} you have deposited {amount} your new balance is {self.balance}'

    def withdraw(self,amount):
        transaction=amount+amount*0.05
        if amount<=0:
            return f'Invalid input'

        elif self.balance<=transaction:
            return f'Insufficient balance'

        else:
             self.balance-=transaction
             transact={"amount":amount,"balance":self.balance,"narration":"You withdrew","time":datetime.now()}
             self.transactions.append(transact)
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
            transact={"amount":amount,"balance":self.balance,"narration":"You borrowed","time":datetime.now()}
            self.transactions.append(transact)
            return f'You new balance is {loan}. Repay {total_loan} in 30 days'
    def repay(self,amount):
        
        if(amount<=0):
            return f'Invalid input'
        elif(amount>self.loan):
            diff=amount-self.loan
            self.balance+=diff
            return f'Loan has been fully payed, your new account balance is {self.balance}'

        else:
            diff=self.loan-amount
            
            transact={"amount":amount,"balance":self.balance,"narration":"You repayed","time":datetime.now()}
            self.transactions.append(transact)
            return f'{amount} has been deducted to repay your loan outstanding debt is {diff}'

    def statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            specific=time.strftime("%-I:%M%p")
            print(f'On {date} at {specific}..{narration}..{amount}..your account balance is {balance}')


