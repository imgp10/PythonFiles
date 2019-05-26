# FOR LOOP
inp = input('Enter your name \n')
print("Welcome %s" % inp)
num = int(input('Please enter a number in the range 1-10. This is your first attempt. You have a maximum of 5 attempts. \n'))

for a in range(1,5):
    from random import randint as r
    if num == r(1,10):
        print("Well done, you made the right guess in attempt no. %s" % a)
        break
    
    else:
        print("Wrong guess. Re-enter a number. This is your attempt no. %s" % (a+1))
        num = int(input())


if a < 4:
    print('You won the game')

else:
    print('You lost the game')
    
print('You have completed the game')    




# WHILE LOOP
'''
i = 1
inp = input('Enter your name \n')
print("Welcome %s" % inp)
num = int(input('Please enter a number in the range 1-10. This is your first attempt. You have a maximum of 5 attempts. \n'))

while i <= 5:
    from random import randint as r
    if num == r(1,10):
        print("Well done, you made the right guess in attempt no. %s" % i)
        break

    else:
        print("Wrong guess. Re-enter a number. This is your attempt no. %s" % (i+1))
        num = int(input())
        i += 1

print('You have completed the game')
'''

