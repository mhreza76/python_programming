# Sets are used to store multiple items in a single variable
# Duplicates not allowed
# unordered and unindexed
# Set items are unchangeable, but you can remove items and add new items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)

print("\nUpdate set items:")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# The object in the update() method does not have to be a set, it can be any iterable
# object (tuples, lists, dictionaries etc.)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


print("\nRemove set items:")
thisset.remove("banana")
thisset.discard("banana")
print(thisset)

x = thisset.pop()
print(x)
thisset.clear()
print(thisset)

print("\nUnion set items:")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print("\nIntersection set items:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)

# The symmetric_difference method will keep only the elements that are NOT present in both sets.
print("\nsymmetric_difference set items:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x.symmetric_difference_update(y)
print(x)


