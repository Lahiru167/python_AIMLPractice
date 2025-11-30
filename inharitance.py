class parent:
    def fun1(self):
        print("Hello")

class child(parent):
    def fun2(self):
        super().fun1()
        print("welcome")

obj = child()
obj.fun2()
