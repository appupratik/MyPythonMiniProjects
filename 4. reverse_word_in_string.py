#Get input from User
str1 = input("Enter String: ")

#split string and make list
str2 = str1.split(" ")

#create dummy list
temp = []

#reverse method using slice method
for i in str2:
    temp.append(i[::-1])
    
#Join string 
str2 = " ".join(temp)

#output
print("\nEntered String :\t", str1)
print("\nReversed String :\t", str2)
