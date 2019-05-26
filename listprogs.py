a = [3,41,76,89,12]

#1 Sum all the items in a list
def sums(a):
    add = 0
    for addn in a:
        add = add + addn
    print(add)

print(sum(a))


#2 Multiply all the items in a list
def mult(a,n):
    for nums in a:
        print(nums*n)

print(mult(a, 3))


#3 Get the largest number from a list
def largest(v):
    largest = None
    for l in v:
        if largest is None or largest < l:
            largest = l
    return largest

print(largest(a))



#4 Get the smallest number from a list

def smallest(v):
    smallest = None
    for l in v:
        if smallest is None or smallest > l:
            smallest = l
    return smallest

print(smallest(a))






    
