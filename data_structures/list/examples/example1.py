l = [1, 2, 3, 4, 5]
print(l)


# Lists in Python must not have to hold the same type of values. Can even have lists inside a list.
l = [1, "Messi", 3.14, True, [5, 6, 7]]
print(l)

# how to check if a value is inside a list
print(6 in l)  # prints False, you can use (6 in l[-1]) to print True, last element of the list
print(6 in l[-1])


# accessing item by index in a list
print(l[1])      # Messi


# accessing an element of a list inside a list
print(l[4][1])     # 6


del l[0]
print(l)
# del l statement deletes the entire list


planets = ["earth", "venus", "mars", "jupyter"]
planets.remove("venus")     # removes venus from the list
print(planets)

