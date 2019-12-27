#input hours and convert to floating point integer
hrs = input("Enter Hours:")
h = float(hrs)

#input pay rate and convert to floating point integer
rate = input("Enter rate per hour:")
r = float(rate)

#factor for overtime if hour input is greater than 40
if h > 40:
    overtime = (h-40)
    overtimeRate = overtime * (1.5*r)

#output calculation results of pay * rate
print (overtimeRate + (r*40))
