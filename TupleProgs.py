#1 CREATING TUPLE
'''
t = 1,2
print(t)


#2 TUPLE WITH DIFFERENT DATA TYPES

u = 1,1.5,'Hi', True
print(u)


#3 TUPLE WITH NO.'s & PRINT ONE ITEM

a = 1,2,3,4,5
print(a[0])


#4 UNPACKING A TUPLE IN SEVERAL VARIABLES

b = 'H', 'e', 'l', 'l', 'o'
print(b)

c = a, b , t, u
print(c)

for i in a:
    print(i)


#5 ADDING AN ITEM TO A TUPLE

for i in range(1):
	l = list(a)
	l.append(6)
	a = tuple(l)
	print(a)


#6 CONVERTING TUPLE TO A STRING

s = str(u)
print(s)



#7 GET 4TH ELEMENT FROM START AND LAST OF A TUPLE

z =  1,2,3,'H', 'e', 'l', 'l', 'o', 1.7, True, False
print(z)

for i in range(1):
    print("%s%s"%(z[3],z[-4]))


#8 CREATE A COLON OF A TUPLE


for i in a,b,t,u:
    print(i, end = ":")

'''

#9 FINDING REPEATED ITEMS OF A TUPLE

f = 1,1,2,4,5,6,7,8,8

def repeated(a):
    e = {}
    for i in a:
        if i not in e:
            e.update({i:a.count(i)})

    for i in e:
        if e.get(i) > 1:
            print(i)
    

repeated(f)




