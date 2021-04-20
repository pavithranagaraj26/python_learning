try:
    a =20
    b =0
    print(a/b)
except ZeroDivisionError:
    print("there is a divide by zero error")
finally:
    print("This is going to excecute no matter what")