class ATM (object):
    def __init__ (self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def start (self):
        print("Started")
    def stop (self):
        print("Stopped")
    def cashWithdrawal (self):
        print("Money Withdrawed")
    def balanceInquiry (self):
        print("You have money in your account!")
person1 = ATM("1234567890101112","1234")
person2 = ATM("1314151617181920","5678")
print(person1.cardNumber)
print(person2.pinNumber)
print(person2.cardNumber)
print(person2.pinNumber)