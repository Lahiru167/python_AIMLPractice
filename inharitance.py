class friut:
    numberOfitems = None
    Unit_price = None
    def set_Value(self,x,y):
        self.numberOfitems=x
        self.Unit_price=y

class apple(friut):
    
    def price(self):
        print("Total price of apple:",self.numberOfitems*self.Unit_price)
class Orange(friut):
    
    def price(self):
        print("Total price of Orange:",self.numberOfitems*self.Unit_price)

class grapes(friut):
    
    def price(self):
        print("Total price of grapes:",self.numberOfitems*self.Unit_price)
        

obj1=apple()
obj2=Orange()
obj3=grapes()

numberOfitems = int(input("Enter number of items of apple: "))
Unit_price = int(input("Enter unit price of apple: "))
obj1.set_Value(numberOfitems,Unit_price)

numberOfitems = int(input("Enter number of items of Orange: "))
Unit_price = int(input("Enter unit price of Orange: "))
obj2.set_Value(numberOfitems,Unit_price)

numberOfitems = int(input("Enter number of items of grapes: "))
Unit_price = int(input("Enter unit price of grapes: "))
obj3.set_Value(numberOfitems,Unit_price)



obj1.price()
obj2.price()
obj3.price()