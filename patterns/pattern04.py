rows = int(input("Enter number of rows: "))

for row in range(rows):
    for col in range(1, row+2):
        print(col, end="")
    print("")