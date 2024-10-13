print("Hello, World!")


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
p = q = r = "APPLE"
print (p)
print (q)
print (r)


# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

# Ex:1 
x = "Ex:1 - Python is awesome"
print(x)

# Ex:2
x = "Ex:2 - Python"
y = "is"
z = "awesome"
print(x, y, z)

# Ex:3
x = "Ex:3 - Python "
y = "is "
z = "awesome"
print(x + y + z)


# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
# print(x + y)

# Global Variable 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)