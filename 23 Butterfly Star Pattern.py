rows = 5

# Upper Part
for i in range(1, rows + 1):
    # Left Stars
    for j in range(i):
        print("*",end="")

    #Spaces
    for j in range(2*(rows - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*",end="")
    print()

# Lower Part
for i in range(rows-1,0,-1):

    #Left stars
    for j in range(i):
        print("*",end="")

    # Spaces
    for j in range(2*(rows - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*",end="")
    print()