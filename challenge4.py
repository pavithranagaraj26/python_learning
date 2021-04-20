#bmicalculator

# weight=float(input("enter the weight in kg:"))
# height=float(input("enter the height in meters:"))

# bmi= (weight)/(height)^2

# print(bmi)


def calcbmi(w,h):
    new_bmi = w/(pow(h, 2))
    return new_bmi

w=float(input("enter the weight in kg:"))
h=float(input("enter the height in meters:"))

bmi=calcbmi(w,h)
print(bmi)