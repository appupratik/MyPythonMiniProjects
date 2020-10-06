#Get the input value from user to find Prime Numbers from 0 to <UserInputValue>

#getting Starting number and Ending number from User
num = input("Enter Starting Number: ")
num1 = input("Enter Ending Number: ")

#create list for storing result
result = []

#if the both entered value is integer then string is run else 
if num.isdigit() and num1.isdigit():
    for r in range(int(num),int(num1)):
        if r > 0:  
           for i in range(2,r):  
               if (r % i) == 0:    
                   break  
           else:  
               result.append(r)
    print(result)
else:
    print("\nEnter Numbers only")




