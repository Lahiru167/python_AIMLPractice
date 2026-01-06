def avg_mark():
    makres = []
    count=1
    total=0
    
    while count<=10:
        mark=int(input("Enter mark:"))
        makres.append(mark)
        total=total+mark
        count+=1
    
    max_mark=makres[0]
    min_mark=makres[0]
    
    i=1
    while i<len(makres):
        if makres[i]>max_mark:
            max_mark=makres[i]
        if makres[i]<min_mark:
            min_mark=makres[i]
        i+=1
    avg=total/10
    print("Average mark:",avg)
    print("Maximum mark:",max_mark)
    print("Minimum mark:",min_mark)
    
    
avg_mark()