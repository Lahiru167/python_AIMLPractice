fruits=["apple","banan","orange"]

for fruit in fruits:
    print(fruit)

print("-------------------------------------")
    
for i in range(10):
    print(i)
    
print("-------------------------------------")
num = 5

while num>0:
    print(num)
    num -=1
print("out side loop")
print("-------------------------------------")


for i in range(10):
    if i==5:
        break
    print(i)
print("out side loop")
print("-------------------------------------")

for i in range(10):
    if i==5:
        continue
    print(i)
print("out side loop")
print("-------------------------------------")

for i in range(10):
    if i%2 ==0:
        continue
    print(i)
print("out side loop")
print("-------------------------------------")

for i in range(10):
    if i%2 !=0:
        continue
    print(i)
print("out side loop")
print("-------------------------------------")

for i in range(10):
    if i%2 ==1:
        continue
    print(i)
print("out side loop1")
print("-------------------------------------")
