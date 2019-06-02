#1 WRITE-APPEND-READ A FILE
def write(a, b):
    a = '%s' % a
    f = open(a, 'w')
    f.write(b)
    f.close()

    

def append(a, b):
    a = '%s' % a
    f = open(a, 'a')
    f.write(b)
    f.close()

    

def read(a):
    a = '%s' % a
    f = open(a, 'r')
    print(f.read())




#2 WRITE-APPEND-READ A FILE USING OS & PYPERCLIP MODULES

import os

path = os.getcwd() + '\\hw'
os.mkdir(path)
os.chdir(path)

write('assignment.txt', "Hello\n")
append('assignment.txt', "Gaurav here")

def readp(a):
    import pyperclip as p
    a = '%s' % a
    f = open(a, 'r')
    p.copy(f.read())
    print(p.paste())

readp('assignment.txt') 

