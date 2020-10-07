#Two sorted list given with different Lenghts
list1 = [10,20,30,40,50,60,70]
list2 = [5,15,25,35,36,37,38,39,45,51,55,65,71,80]

#create List for Result
list3 = []

#using while loop for when list1 is true and list2 is true
while list1 and list2:
    #check which item is greater and less. Less value is append to list3
    if list1[0] <= list2[0]:
        i = list1.pop(0)
        list3.append(i)
    else:
        i = list2.pop(0)
        list3.append(i)

#remaining items are append to list3
list3.extend(list1)
list3.extend(list2)

#Result List
print(list3)