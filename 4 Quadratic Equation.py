import math
a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))

d = b**2-4*a*c

if d> 0:
    root1 = (-b+math.sqrt(d)) / (2*a)
    root2 = (-b-math.sqrt(d)) / (2*a)

elif d == 0:
    root = -b /(2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex root:",real,"+", imag, "iand",real,"-",imag,"i")