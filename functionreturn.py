def add(a,b):
    c = a+b
    return c
# add(100,200)
result = add(100,200)
print(result)

#passonefunction as args to another function
def add1(a,b):
    return a + b

def square(c):
    return c*c

final=square(add1(5,10))
print(final)