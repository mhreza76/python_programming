#assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

#assign multiple variables with same value
x = y = z = "Orange"
print(x, y, z)

global_x = "global x"
global_y = "global y"

def globalVariable():
    #only update locally
    global_x = "local x"
    print(global_x)

    #global keyword refer to the variable globally
    global global_y
    global_y = "local y"
    print(global_y)

globalVariable()
print(global_x)
print(global_y)

username = input("Enter username:")
print("Username is: " + username)


