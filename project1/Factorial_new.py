def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)

def print_factorial(n):
    result = factorial(n)
    print(f" factoral of {n} is {result}")
    
    i =1
    while i <=n:
        print(f"{i}! = {factorial(i)}")
        i+=1

num = int(input("Enter number: "))
print_factorial(num)