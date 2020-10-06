#getting Starting number and Ending number from User
num = input("Enter Starting Number: ")
num1 = input("Enter Ending Number: ")

result = []

#if the both entered value is integer then string is run else 
if num.isdigit() and num1.isdigit():
#check the entered values has difference or not
    if int(num)<int(num1):        
        for i in range(int(num),int(num1)+1):
            order = len(str(i))
            sum = 0
 
            temp = i
            while temp > 0:
                digit = temp % 10
                sum += digit ** order
                temp //= 10
                
            if i == sum:
                #print('First Armstrong Number is ',i)
                result.append(i)
                check = len(result)
                if check >4:
                    break

#the first value is greater than second value then gives this message        
    else:
        print("Second Value is Lowerthan First Value")
else:
    print("\nEnter Numbers only")

#Another condition for display result else disply "No Result Found"
if len(result)>0:
    print(f'First "{len(result)}" Armstrong Number Between "{num}" and "{num1}"')
    print("\n",result)
else:
    print(f'\nNo Armstrong Number Found Between "{num}" and "{num1}"')
