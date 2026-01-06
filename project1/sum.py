def func():
    total=0
    
    number=int(input("Enter number:"))
    
    while number!= -999:
        total=total+number
        number=int(input("Enter number:"))
    print("Sum:",total)
    
func()
