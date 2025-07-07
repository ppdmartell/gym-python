def do_something(num1=7, num2=8) -> float:     # The -> float part is optional, for explicit return type)
    return num1 * num2                         # mainly for readability 

def do_something_simplified(num1=7, num2=8):
    return num1 * num2


print(do_something())
print(do_something(1))
print(do_something(4,9))


print(do_something_simplified())
