# Creating variable
x=5
y="truong"
v='chau'
print(x)
print(y)
print(v)
print("-----------------------------------")

# Casting
z=str(3)
print(type(z))
print("-----------------------------------")

# Many values to multiple variables
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)
print("-----------------------------------")

# One value to multiple variables
j=k=l="Orange"
print(j)
print(k)
print(l)
print("-----------------------------------")

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
q,w,e = fruits
print(q)
print(w)
print(e)
print("-----------------------------------")

# Output variables
# str + str => TRUE
firstName="Truong"
lastName="Chau"
print(firstName + lastName)

# int + int => TRUE
num1=5
num2=10
print(num1+num2)

# str + int => FALSE
# print(num1+firstName) => ERROR
print("-----------------------------------")

# Global variables
o="awesoe" # global variables
def myfunc():
    o="fantastic" # local variables
    print("Python is " + o)

myfunc()

print("Python is " + o)

# Global keyword
def myFunc():
    global x
    x="fantastic"

myFunc()
print("Python is " + x)
print("-----------------------------------")
