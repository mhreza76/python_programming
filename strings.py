
# Multiline Strings
multi_line_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multi_line_string)

# Slicing strings
# start position to end position (end position not included)
# index from 0 and -1
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

mod_strings = " Modify, Strings "
print(mod_strings.upper())
print(mod_strings.lower())

# strip removes starting and ending spaces
print(mod_strings.strip())
print(mod_strings.split(','))
print(mod_strings.replace(" ", "-"))

print("\nString formating:")
# string format
age = 36
txt = "My name is John, I am " + str(age)
print(txt)

age = 26
txt = "My name is John, and I am {}, Graduate in {}"
print(txt.format(age, 2021))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))