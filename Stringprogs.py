'''
#1 Length of a string

def strsize(a):
    count = 0
    for i in a:
        count = count + 1
    print(count)


#2  Frequency count in s = 'google.com' for each letter

s = 'google.com'
e = {}

for i in s:
	if i not in e:
		e.update({i:s.count(i)})



#3 Get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string



def text(inp):
    try:
        if len(inp) > 2:
            print("%s%s%s%s"%(inp[0],inp[1],inp[-2],inp[-1]))
        elif len(inp) == 2:
            print(inp*2)
        else:
            print('Empty String')
    except:
        print('Enter a string')


text('w3resource')


#4 Get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

a = 'restart'

def repeat(a):
        a = list(a)
        for i in range(1, len(a)):
                if a[0] ==  a[i]:
                        a[i] = '$'
                        

        for i in a:
            print(i, end = "")
            
repeat(a)




#5 Get a single string from two given strings, separated by a space and swap the first two characters of each string


def text1(a,b):
	print("%s%s%s %s%s%s"%(b[0], b[1], a[-1], a[0], a[1], b[-1]))




#6
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3)
# If the given string already ends with 'ing', then add 'ly' at the end.
# If the string length of the given string is less than 3, leave it unchanged

def ingly(inp):
    if inp[-3:] == 'ing':
        print("%s%s%s"%(inp, 'l', 'y'))

    elif len(inp) >= 3:
            print("%s%s%s%s" % (inp, 'i', 'n', 'g'))

    elif len(inp) < 3:
        print(inp)



#8 Python function that takes a list of words and returns the length of the longest one

l = ['Athens', 'Rome', 'Johannesburg', 'Zurich']

def maximum(a):
    e = {}
    for i in range(len(a)):
        if a[i] not in e:
            e.update({a[i]:len(a[i])})

    return max(e.values())



print(maximum(l))
'''

#10 Exchanging first and last character of a word

def exchange(v):
    z = list(v)
    z[0] = v[-1]
    z[-1] = v[0]
    for i in z:
        print(i, end = "")
    
    


