#input hours and convert to floating point integer
def hours():
    try:
        hrs = input("Enter Hours:")
        h = float(hrs)
        return h
    except:
        print ("Please enter an integer")
        hours()
h = hours()
#input pay rate and convert to floating point integer
try:
    rate = input("Enter rate per hour:")
    r = float(rate)
except:
    print ("Please enter an integer")

#factor for overtime if hour input is greater than 40 and print result
if h > 40:
    overtime = (h-40)
    overtimeRate = overtime * (1.5*r)
    print (overtimeRate + (r*40))

#skip the if statement when pay <= 40 and print pay rate at standard rate interval
else:
    print (h * r)
