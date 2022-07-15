#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

#Prevent a user from creating an object of that class
#+ compels a user to override abstract methods in a child class 

from abc import ABC, abstractmethod

class Banking(ABC):

    def __init__(self, checking, savings):
        self.checking = checking
        self.savings = savings

    @abstractmethod
    def view_checking():
        pass
    
    @abstractmethod
    def view_savings():
        pass

    @abstractmethod
    def make_transfer_to_savings():
        pass


class Operation(Banking):

    def view_checking(self):
        print(f"Your checking account has a balance of ${self.checking}")

    def view_savings(self):
        print(f"Your savings account has a balance of ${self.savings}")

    def make_transfer_to_savings(self, transfer_amount):
        print(f"${transfer_amount} will be transfered from your checking account to your saving account")
        self.checking -= transfer_amount
        self.savings += transfer_amount
        return self.view_savings(), self.view_checking()

money = Operation(300, 1000)
money.view_checking()
money.view_savings()
money.make_transfer_to_savings(200)


