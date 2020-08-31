def computepay(h,rate):
    if(h > 40):
        extra = h - 40
        extra = extra * (rate * 1.5)
        rate = 40 * rate
        pay = rate + extra
        return pay
    else:
        pay = h * rate
        return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    rate = float(rate)
except:
    print('Enter Numeric Number')
print('Pay',computepay(h,rate))

