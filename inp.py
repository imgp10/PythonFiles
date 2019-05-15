
inp1 = input("Enter hrs\n")

try:
    hrs = float(inp1)
    n = 40
    if hrs <= 40:
        pay = hrs*10
        print(pay)
    elif hrs > 40:
        pay = n*10 + (hrs-n)*15
        print(pay)
        
except:
    print('Wrong input. Enter a number')


'''
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
'''

