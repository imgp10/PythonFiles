#1 TABLE OF 10

for a in range(1,11):
    b = 10*a
    print("%s X %s = %s" % (10,a,b))


#2 TABLE BASED ON VALUE INPUT BY THE USER

d = int(input('Enter value\n'))
for c in range(1,11):
    e = d*c
    print("%s X %s = %s" % (d,c,e))


#3 TABLES OF 1 UPTO THE VALUE INPUT BY THE USER
b = int(input('Enter Value\n'))

for n in range(1, b+1):
    for m in range(1,11):
        q = n*m
        print("%s X %s = %s" % (n,m,q))


