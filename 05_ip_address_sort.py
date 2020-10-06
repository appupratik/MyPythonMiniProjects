#List of IP addresses 
list1 =["192.168.10.9","192.168.10.4","192.168.10.11","192.168.10.35"]

#Create dummy lists
a = []
b = []

#split Ip appress from last digit and append in dummy 'a'
def ips(x):
    for i in x:
        l=i.rsplit(".",1)
        a.append(l)

#join list for making full IP address
def joinL(x):
    for i in x:
        l=".".join(i)
        b.append(l)

#Create function for sort Method
def sortL(x):
    return int(x[1])
    
#print Before List    
print("Before:\t",list1)

#split IP with using 'ips' function and append in 'a'
ips(list1)
#shor dummy list 'a' with use of sort method using function 'sortL'
a.sort(key=sortL)
#join 'a' 
joinL(a)
#re-assign list1
list1 = b
print("After:\t",list1)