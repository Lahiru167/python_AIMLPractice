def numcheack(num):

  if num % 2 == 0:
    return "Even"
  else:    
    return "odd"

def main():
    number = int(input("Enter a number: "))
    result = numcheack(number)
    print(f"The number {number} is {result}.")
    

main()