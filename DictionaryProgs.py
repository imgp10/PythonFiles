#2 ADDING A KEY TO A DICTIONARY


# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d = {0:10, 1:20}
print(d)
d[2] = 30
print(d)


#3 CONCATENATING DICTIONARIES TO CREATE A NEW ONE

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}


dic1.update(dic2)
dic1.update(dic3)
print(dic1)



#5 ITERATING OVER A DICTIONARY USING FOR LOOP

for i in dic1, dic2, dic3:
    print(i)


#6 Dictionary that contains a number (between 1 and n) in the form (x, x*x). 

n = int(input('Enter a number \n'))
d1 = {}
for i in range(1,n+1):
    if i not in d1:
        d1.update({i:i**2})
print(d1)


#7 Dictionary where the keys between 1 and 15 (both included) and the values are square of keys

d2 = {}
for i in range(1,16):
    if i not in d2:
        d2.update({i:i**2})
print(d2)



#8 MERGING 2 PYTHON DICTIONARIES

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

dict1.update(dict2)
print(dict1)


