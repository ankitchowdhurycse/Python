rows = int(input("Enter number of rows: "))

for row in range(rows):
    for col in range(row+1):
        print("*", end="")
    print("")