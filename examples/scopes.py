var = "This is a global variable"

def do():
    print("Entering method do()")
    var = "This is a local variable"    # totally different variable

def change_global():
    print("var now, about to change")
    global var
    var = "Changed value of var with global keyword"

do()
print(var)    # will print "This is a global variable"

change_global()
print(var)
