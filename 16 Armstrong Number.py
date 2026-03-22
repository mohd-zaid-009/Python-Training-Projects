num = int(input("Enter a number:"))
original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")