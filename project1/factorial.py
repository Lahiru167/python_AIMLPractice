num =int(input("Enter number: "))
factorial = 1
i = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    while i <=num:
        factorial *=i
        i +=1
    print(f"The factorial of {num} is {factorial}")
    