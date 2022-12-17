class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def __str__(self):
        return f"{self.firstname}({self.lastname})"

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
print(x)
x.printname()
