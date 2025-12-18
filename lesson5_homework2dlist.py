l1 = []
row = int(input("How many rows do you want"))
column = int(input("How many columns do you want"))

for i in range(row):
    row_list = []
    for j in range(column):
        value = int(input("Enter your numbers at [{}][{}]".format(i,j)))
        row_list.append(value)
    l1.append(row_list)

for i in range(row):
    for j in range(column):
        print(l1[i][j], end=" ")
    print("\n")

