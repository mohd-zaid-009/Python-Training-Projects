a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a>b and a>c:
    print(f"{a} number is largest")
elif b>a and b>c:
    print(f"{b} number is largest")
else:
    print(f"{c} number is largest")
