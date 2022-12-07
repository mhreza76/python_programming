# Tuples are used to store multiple items in a single variable
# Allow Duplicates
# ordered
# unchangeable

mytuple = ("apple", "banana", "cherry")
print(mytuple[0])
print(mytuple)

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

print("\nUnpacking a tuple:")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print(type(red))

print("\n")
print(fruits)
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)