print("Hello World!")

var = 7
var1 = var
var = 10
print(var1)


# String slice
var = "tomato"
print(var[:4])
print(var[3:4])
print(var[:])
print(var[3:])


# using type()
print(type(var))

# using str()
number = 3.14
number1 = str(number)
print(number)
print(number1)
print(type(number))
print(type(number1))

# input
number = int(input("Enter an int: "))
print(number)
print(type(number))

number1 = float(input("Enter a float: "))
print(number1)
print(type(number1))

text = input("Enter a string: ")
print(text)
print(type(text))

