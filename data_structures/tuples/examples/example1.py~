t0 = (0, 0, 1, 1, 1)

# in order to use the tuple function, it must be used on an iterable parameter
t1 = tuple([5, 3, 'Sun', 45.3])          # on a list
t2 = tuple('Digimon')                    # on a string
t3 = tuple({1: 3, 4: "dictionary"})      # on a dictionary, it get's the keys only

print(t0)
print(t1)
print(t2)
print(t3)
print(t1[:2])                            # you can slice a tuple


# tuples take less space in memory than lists (output in bytes)
print([1, 2, 3].__sizeof__(), 'bytes')
print((1, 2, 3).__sizeof__(), 'bytes')


t4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t4[::-1])     # this prints a slice of the tuple, but it's actually the tuple backwards
print(t4[::2])      # odds only from 1 (because 1 is the first element, otherwise it would start by 0, 2, 4, ...)
print(t4[1::2])     # even only from 2
