try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("\nelse keyword to define a block of code to be executed if no errors were raised:")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("\nThe finally block, if specified, will be executed regardless if the try block raises an error or not.")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished\n")

try:
  x = 10
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


print("\nRaise an exception:")
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
