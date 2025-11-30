class parent:
    def fun1(self):
        print("Hello")

class child(parent):
    def fun2(self):
        print("welcome")
    def fun1(self):
        print("Hi")

obj = child()
obj.fun1()
