# Python for everyone
## Reserved words
| ---    | ---    | ---    | ---    | ---      |
| ------ | ------ | ------ | ------ | -------- |
| False  | class  | return | is     | finally  |
| None   | if     | for    | lambda | continue |
| and    | def    | form   | while  | nonlocal |
| as     | elif   | try    | or     | yield    |
| assert | else   | import | pass   |
| break  | except | in     | raise  |

## Numeric Expressions
| Operator | Operation      |
| -------- | -------------- |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| **       | Power          |
| %        | Remainder      |

#### Python3: when we use division its autometicly forcefully converted to float 

## Operator Precedence
![image](operator_precedence.JPG)
### Example
![image](numeric_operator.JPG)

### Concatenate
```python
name = 'Mahmudul ' + 'Hasan ' + 'Reza'
print(name)
```
#### output
```python
Mahmudul Hasan Reza
```
### Type
```python
print(type(1))
print(type(1.03))
print(type(name))
```
#### output
```python
<class 'int'>
<class 'float'>
<class 'str'>
```

### Type Conversions
```python
print(float(99) + 100)
i = 40
f = float(i)
print(f)
print(type(f))
```
#### output
```python
199.0
40.0
<class 'float'>
```
### string conversion 
```python
s = '123'
ss = int(s) + 1
print(ss)
print(type(ss))
```
#### output
```python
124
<class 'int'>
```
### user input
```python
l_name = input("whats your last name?\n")
print('welcome', l_name)
```
#### output
```python
whats your last name?
Reza
welcome Reza
<class 'int'>
```

**# Every user input we have to convert(type conversion) to our desire data type because python always takes input as string**

**2.2** Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

```python
name = input("Enter your name")
print("Hello", name)
```
#### output
```python
# input
Sarah

# output
Hello Sarah
```
**2.3** Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

```python
hrs = input("Enter Hours:")
hrs = int(hrs)
rate = input("Enter Rate:")
rate = float(rate)
pay = hrs * rate
print('Pay:', pay)
```
#### output
```python
# input
35
2.75

# output
Pay: 96.25
<class 'int'>
```
