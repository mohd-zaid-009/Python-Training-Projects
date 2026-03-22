rows = 4
for i in range(1, rows + 1):
    for j in range(1,2*i):
        print((i + j)% 2, end="")
    print()