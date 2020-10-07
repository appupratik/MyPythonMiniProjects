#Question 1
#The SHIELD is a secretive organization entrusted with the task of guarding the world against any disaster. Their arch nemesis is the organization called HYDRA. Unfortunately some members from HYDRA had infiltrated into the SHIELD camp. SHIELD needed to find out all these infiltrators to ensure that it was not compromised. Nick Fury, the executive director and the prime SHIELD member figured out that every one in SHIELD could send a SOS signal to every other SHIELD member he knew well. The HYDRA members could send bogus SOS messages to others to confuse others, but they could never receive a SOS message from a SHIELD member. Every SHIELD member would receive a SOS message ateast one other SHIELD member, who in turn would have received from another SHIELD member and so on till NickFury. SHIELD had a sophisticated mechanism to capture who sent a SOS signal to whom. Given this information, Nick needed someone to write a program that could look into this data and figure out all HYDRA members.

#Sample Input
'''
Nick Fury : Tony Stark, Maria Hill, Norman Osborn
Hulk : Tony Stark, HawkEye, Rogers
Rogers : Thor,
Tony Stark: Pepper Potts, Nick Fury
Agent 13 : Agent-X, Nick Fury, Hitler
Thor: HawkEye, BlackWidow
BlackWidow:Hawkeye
Maria Hill : Hulk, Rogers, Nick Fury
Agent-X : Agent 13, Rogers
Norman Osborn: Tony Stark, Thor
'''
#Sample Output
#Agent 13, Agent-X, Hitler


#first create dictionary with key and list of values pairs
dict1 = {   'Nick Fury': ['Tony Stark', 'Maria Hill', 'Norman Osborn'],
            'Hulk' : ['Tony Stark', 'HawkEye', 'Rogers'],
            'Rogers' : ['Thor'],
            'Tony Stark': ['Pepper Potts', 'Nick Fury'],
            'Agent 13' : ['Agent-X', 'Nick Fury', 'Hitler'],
            'Thor': ['HawkEye', 'BlackWidow'],
            'BlackWidow':['Hawkeye'],
            'Maria Hill' : ['Hulk', 'Rogers', 'Nick Fury'],
            'Agent-X' : ['Agent 13', 'Rogers'],
            'Norman Osborn': ['Tony Stark', 'Thor']
            }

#create dummy lists for temp work
list1 = []
list2 = []

#append starting value in list of tuple (name, expression)
list1.append(('Nick Fury',1))

#enter first level values
for el in dict1['Nick Fury']:
    list1.append((el,0))
    
#Calling sub level values    
for k,v in enumerate(list1):
    if list1[k][1] == 0:
        temp = list(list1[k])
        temp[1] = 1
        list1[k] = tuple(temp)
        if list1[k][0] in dict1.keys():
            for el in dict1[list1[k][0]]:
                addVal = 0
                for item in list1:
                    if item[0] == el:
                        addVal = 1
                        break

                if addVal == 0:
                    list1.append((el,0))

#find all keys of dict1
for key in dict1.keys():
#find all values of keys of dict1
    for val in dict1[key]:
        list2.append(val)
#remove duplicate values from list using set method
list2 = list(set(list2))

#extract final list and expression value from list1 using zip function
final_list, addVal = zip(*list1)
#convert final_list to List from Tuple
final_list = list(final_list)
   
for person in final_list:
    list2.remove(person)

#sort List for desired output
list2.sort()

print ('\nMembers of HYDRA are:')
a = 1
for i in list2:
    print("\t",a,i)
    a +=1