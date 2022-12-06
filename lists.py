# Lists are used to store multiple items in a single variable
# Allow Duplicates
# ordered
# changeable
#
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

# note the double round-brackets
thislist = list((10.2, "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["watermelon", "banana"]
print(thislist)
thislist[1:3] = ["cherry"]
print(thislist)


# Add items
thislist.insert(1, "watermelon")
print(thislist)
thislist.append("orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# remove items
thislist.remove("orange")
print(thislist)

thislist.pop(0)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

print("\nIterate using for loop\n")
for x in thislist:
  print(x)

print("\nIterate using hort hand for loop\n")
[print(x) for x in thislist]

print("\nIterate using while loop\n")
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("\nIterate using index\n")
for i in range(len(thislist)):
  print(thislist[i])


# The del keyword can also delete the list completely
del thislist



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# List Comprehension
newlist = [x for x in fruits if "a" in x]


# Sort Lists
# SORT Case sensitive
print("\nSort ascending")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("\nSort descending")
thislist.sort(reverse = True)
print(thislist)


print("\nCustom : Sort the list based on how close the number is to 50:")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("\nPerform a case-insensitive sort of the list:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print("\nReverse the order of the list items:")
thislist.reverse()
print(thislist)


# Copy Lists
print("\nMake a copy of a list:")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

