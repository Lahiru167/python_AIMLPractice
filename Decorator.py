

def new(func):
    def inside(a,b):
        if b == 0:
            a,b = b,a
            return func(a,b)
    return inside

def Devide(a,b):
    return a/b


Devide = new(Devide)


print(Devide(5,0))