# ARITHMETIC OPERATORS

a = 1+4   # addition
print(a)

b = 2-7   # subtraction
print(b)

c = 9*6   # multiplication
print(c)

d = 10/5  # divison
print(d)

f = 100%9 # modulo division
print(f)

g = 13//4 # floor division
print(g)

e = 2**5  # exponentiation
print(e)


# LOGICAL OPERATORS

h = True and False  # And
print(h)

i = True or False   # Or
print(i)

j = not True        # Not
print(j)

# COMPARISONS

k = 4 > 3           # Greater
print(k)

l = 4 >= 3          # Greater than or equal to
print(l)

m = 10 < 12         # Less than
print(m)

n = 12 <= 11        # Less than or equal to
print(n)

o = 113 != 'hi'     # Not equal to
print(o)

p = 113 == 113      # Equals
print(p)




# ASSIGNMENT OPERATORS

q = a
q += 5   # q = 10
print('The answer is',q)


r = b
r -= 5   # r = -10
print('The answer is',r)

s = c
s *= 3   # s = 162
print('The answer is',s)

t = d
t /= 2   # t = 1
print('The answer is',t)

u = e
u **= 2  # u = 1024
print('The answer is',u)

v = f
v %= 3   # v = 1
print('The answer is',v)

w = g
w //= 2  # w = 1
print('The answer is',w)



# IDENTITY OPERATORS

x = int(input('Enter first value?\n'))
y = int(input('Enter second value?\n'))

print(type(x) is int)
print(x is not y)


# MEMBERSHIP OPERATORS

z1 = "Hello!"
print('H' in z1)
print('He' in z1)
print('Ho' in z1)

z2 = input('Enter text \n')
print(z2)
print('B' not in z2)
print('e' not in z2)


# IF-ELIF-ELSE STATEMENTS

a1 = 3
if a1%2 == 0 :
    print('Even number')
else :
    print('Odd number')


a2 = 0
if a2 > 0:
    print('Positive')
elif a2 < 0:
    print('Negative')
else:
    print('Zero')


a3 = ""
if a3 == "" :
    print('Falsey value')
else :
    print('Truthy value')





# IN-BUILT FUNCTIONS

b1 = input('Enter Text\n')
print(len(b1))  # length
print(max(b1))  # max
print(min(b1))  # min

  
print(int(3.45))      # Converts to type integer
print(float('-12'))   # Converts to type float
print(str(13))        # Converts to type str

