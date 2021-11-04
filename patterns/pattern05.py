rows = int(input("Enter number of rows: "))

for row in range(rows):
    for col in range(row+1):
        print("*", end="")
    print("")
for row in range(rows-1, 0, -1):
    for col in range(row, 0, -1):
        print("*", end="")
    print("")