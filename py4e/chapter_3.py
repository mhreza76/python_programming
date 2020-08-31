str = 'reza'
try:
    s_to_int = int(str)
except:
    s_to_int = -1
print(s_to_int)

str = '123'
try:
    s_to_int = int(str)
except:
    s_to_int = -1
print(s_to_int)


# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    rate = float(rate)
except:
    print('Enter Numeric Number')
if(h > 40):
    extra = h - 40
    extra = extra * (rate * 1.5)
    rate = 40 * rate
    pay = rate + extra
    print(pay)
else:
    pay = h * rate
    print(pay)

'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''
score = input('Enter score: ')
try: 
    score = float(score)
except:
    print('Enter a numeric number')
if(score > 1.0):
    print('Inputed Score is out of range')
elif(score >= 0.9 and score <= 1.0):
    print('A')
elif(score >= 0.8):
    print('B')
elif(score >= 0.7):
    print('C')
elif(score >= 0.6):
    print('D')
elif(score < 0.6 and score >= 0.0):
    print('F')
else:
    print('Inputed Score is out of range')

