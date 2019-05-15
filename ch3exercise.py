'''
inp1 = input("Enter hrs\n")

try:
    hrs = float(inp1)
    if hrs <= 40:
        pay = hrs*10
        print(pay)
    else:
        pay =  400+ 15*(hrs-40)
        print(pay)
        
except:
    print('Wrong input. Enter a number')



score = float(input("Enter number within 0-1\n"))
try:
    if score > 1.0:
        print("Bad score")
    if score >= 0.9 and score <= 1.0:
        print("A Grade")
    elif score >= 0.8 and score < 0.9:
        print("B Grade")
    elif score >= 0.7 and score < 0.8:
        print("C Grade")
    elif score >= 0.6 and score < 0.7:
        print("D Grade")
    elif score < 0.6:
        print("F Grade")

except:
    print("Bad score")

'''


def computepay(hrs,rate):
    try:
        if hrs <= 40:
            pay = hrs*rate
            return(pay)
        else:
            pay = 400 + (hrs-40)*(1.5*rate)
            return(pay)
        
    except:
        print('Enter a number')








