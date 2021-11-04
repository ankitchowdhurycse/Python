rows = int(input("Enter number of rows: "))

for row in range(1, rows+1):
    for col in range(1, rows+1):
        if col <= (rows - row):
            print(" ", end="")
        else:
            print("*", end="")
    print("")