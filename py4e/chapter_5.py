large = None
small = None
count = 1
while True:
     num = input("Enter a number ")
     if num == "done":
          break
          
     try:
          num = float(num)
          if count == 1:
               large = num
               small = num
               count += 1
          if num > large:
               large = num
          if num < small:
               small = num 
     except:
          print('Invalid input')
print('Maximum is', int(large))
print('Minimum is', int(small))
