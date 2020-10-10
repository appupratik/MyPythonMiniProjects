#Random Password Generator Program
#import random module
import random

#create desired output data in list
str1 = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','0123456789','!@#$%^&*']
#create blank list to store output
res1=[]

def generatePwd():
#make sure that desired output list is blank
    res1=[]
    #create for 6 characters from 'A-Za-z' means str1[0]
    for i in range(6):
        a = random.choice(str1[0])
        res1.append(a)
    #create for 4 characters from '0-9' means str1[1]
    for i in range(4):
        a = random.choice(str1[1])
        res1.append(a)
    #create for 2 characters from 'Special Symbols' means str1[2]
    for i in range(2):
        a = random.choice(str1[2])
        res1.append(a)
    #shuffle the list to rearrange the list
    random.shuffle(res1)
    #join list to make string
    return "".join(res1)

#display random password in 4 choice
print("First Random Password is \t: ",generatePwd())
print("Second Random Password is \t: ",generatePwd())
print("Third Random Password is \t: ",generatePwd())
print("Forth Random Password is \t: ",generatePwd())
