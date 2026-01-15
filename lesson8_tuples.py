#tuple 1
#tuples is a type of data structure where we can store different types, but we cannot update a tuple after creation
#in making a tuple, you will not have to worry about putting brackets
tuple_1 = "hello", "guten tag", "caio", "Dia duit"
print(tuple_1)
print(len(tuple_1))
print(tuple_1[3])

#unpacking
#unpacking means shifting the values in a tuple to variables
a,b,c,d = tuple_1
print(a)
print(b)
print(c)
print(d)

#nested tuples
#if I wanted to print hi my index would be : tuple_2[4][0]
tuple_2 = 1,2,3,4,("hi",1)
print(tuple_2[4][0])

#
slice =tuple_1[0:2:1]
print(slice)