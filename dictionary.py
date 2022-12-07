# Dictionary are used to store data in key:value pair
# Duplicates not allow
# ordered
# changeable

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict.get("name"))
print(thisdict.keys())
print(thisdict.values())

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# The items() method will return each item in a dictionary, as tuples in a list.
print(car.items())

if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")


# Add Items
print("\nAdd Items:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


# Remove Items
print("\nRemove Items:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.pop("model")
thisdict.popitem() #remove from last
print(thisdict)


#Loop Through
print("\nLoop:")

print("\nKeys:")
for x in thisdict:
  print(x)

print("\nValues using index:")
for x in thisdict:
  print(thisdict[x])

print("\nValues using values:")
for x in thisdict.values():
  print(x)

print("\nKeys using keys:")
for x in thisdict.keys():
  print(x)

print("\nKeys and Values using items:")
for x, y in thisdict.items():
  print(x, y)

print("\nNested Dictionaries:")
# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child1"]["name"])
