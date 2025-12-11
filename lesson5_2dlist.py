l1 = []
row = int(input("How many rows do you want?"))
column = int(input("How many colums do you want?")) 
#for taking an input for a matrix we need to first ask the rows and columns in this case our matrix is l1

for i in range (row):
    row_list = []
    for j in range(column):
        value = int(input("Enter the number"))
        row_list.append(value)

    l1.append(row_list)

# printing the elements of a matrix

for i in range (row):
    for j in range(column):
        print(l1[i][j], end = " ")
    print("\n")

#by default the computer moves every number to the next line they way we put full stops at the end of our sentence before starting a new one
#doing end keeps all the numbers in our 2-d list in one line
#\n divides the lines into their own divisions via the list l1

l2 = [[2,3],[4,5],[6,7],[8,9]]

print(len(l2))# this instruction gives you the number of rows
print(len(l2[0]))# this instruction gives you the number of columns
print(l2[2][0])


