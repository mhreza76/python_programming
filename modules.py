
import mymodule as mx
mx.greeting("Reza")
print(dir(mx))

import datetime as dt
x = dt.datetime.now()
print(x.year)
print(x.strftime("%A"))


import math
x = math.ceil(1.4)
y = math.floor(1.4)


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)