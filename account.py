
class account:
    def __init__(self,id=0,bal=100,ar=0):
        self.__id=id
        self.__bal=bal
        self.__ar=ar
        
    def getMonthlyInterestRate(self):
        return self.__ar/12
    def getmonthlyinterest(self):
        return self.getMonthlyInterestRate()*self.__bal 
    def withdraw(self):
        wd=float(input("Enter amount to be withdrawn"))
        self.__bal-=wd 
        self.getbalance()
    def deposit(self):
        dp=float(input("Enter amount to be deposited"))
        self.__bal+=dp 
        self.getbalance()
    def getbalance(self):
        print("balance:",self.__bal)
    def getid(self):
        print("ID:",self.__id)    
a1=account(1122,20000,4.5)
a1.getbalance()
print("Monthly interest rate:",a1.getMonthlyInterestRate())
print("Monthly interest:",a1.getmonthlyinterest()) 

a1.withdraw()
a1.deposit()

  