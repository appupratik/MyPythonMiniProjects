#List with data with '0'
list1=[1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,210,1,2,0,45]
print("\nBefore:\t",list1)
#sort list
list1.sort()

#define function to append values in two dummy functions "0" in first function and other in second function
def zeroEnd(x):
    a=[]
    b=[]
    for i in x:
        if i == 0:
            a.append(0)
        else:
            b.append(i)
# extend list b with list a
    b.extend(a)
    
#return function as list b    
    return b

list1 = zeroEnd(list1)
print("After:\t",list1)