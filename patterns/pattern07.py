rows = int(input("Enter number of rows: "))

for row in range(rows):
    for col in range(rows):
        if col < row:
            print(" ", end="")
        else:
            print("*", end="")
    print("")