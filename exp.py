'''
n = input()

if type(n) is int:
    k = int(n)
elif type(n) is str:
    print("Please enter a numeric value")
    m = int(input())
    o = m + 5
    print(o)
'''


'''
fruit = 'banana'

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
'''   

'''
index = len(fruit)-1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1



for char in fruit:
    print(char)
'''


## MULTIPLYING EACH ELEMENT OF A LIST
l = [1,2,3,4,5]

index = 0
while index < len(l):
    number = l[index] * 5
    print(number)
    index += 1


for n in range(len(l)):
    num = l[n] * 10
    print(num)






