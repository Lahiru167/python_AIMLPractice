def func():
    count=1
    
    while count<=5:
        mark=int(input("Enter mark:"))
        if mark>=75:
            print("A")
        elif mark>65 & mark<75:
            print("B")
        elif mark>55 & mark<64:
            print("C")
        elif mark>45 & mark<54:
            print("s")
        else:
            print("F")
        count+=1

func()
            
        
        
        