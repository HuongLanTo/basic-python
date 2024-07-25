# Creating
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

# Casting
x = str(3)
y = int(3)
z = float(3)

# Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)