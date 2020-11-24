import random

num1 = int(input("Enter Range to: "))

list1=list(range(1,num1+1))

print(list1)

for i in range(len(list1)):
    input("Press Enter Key for Next Number")
    a = random.choice(list1)
    print(a)
    list1.remove(a)

