# the unique parts of sets are that they do not allow duplicates within them and they are unordered meaning you can add and remove elements
set1 = {1,2,3,4,5}
print(set1)

l1 = (1,2,3,4,5)
set2 = set(l1) # set is a function
print(set2)
set2.add(6)
set2.update([7,8]) #if duplicates occur the python programme will delete them for you
#if you try to remove an element that doesn't exist it will give an error
#to prevent this kind of error use ____ .discard()
set2.remove(8) 
set2.pop()#.pop removes one random element
print(set2)
#set2.clear()   #.clear removes everything

s1 = {1,2,3}
s2 = {4,5,6}
#.union means the union of sets
print(s1.union(s2))
#.intersection  = common elements between two sets
print(s1.intersection(s2))
#.difference = elements that are existing in set1 but not in set2
#.symmetric_difference = the union of sets minus the intersection
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

for element in s1:
    print(element)

if 3 in s1 :
    print("element is in this set")
else:
    print("element is not in this set")