#find how many character comes in string and which character is comes highest
#Getting input from User
str1 = input("Enter String: ")

#Convert string to list with use of set to remove Similler character and also convert string to lower-case to check only characters
test = list(set(str1.lower()))

#sort the list
test.sort()

#create dummy list and dictionary
result = {}

#Getting input in dummy dictionary
for i in test:
    a = str1.count(i)
    result[i] = a

print('\nHow many times Characters come in string')
for k,v in result.items():
    print(k,":",v)
print('\n')

#Find character which come in maximum times
a = max(result.values())
print('\nThis character(s) comes in Maximum Time(s)')
for k,v in result.items():
    if v == a:
        print(k,":",v)
