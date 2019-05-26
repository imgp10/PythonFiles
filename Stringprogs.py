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




            
