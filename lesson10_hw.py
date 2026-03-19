string1 = input("Type your numbers")
def panagram(string1):
    s1 =set("1234567890")
    s2 = set()

    for s in string1:
        if string1.isdigit():
            s2.add(s)

    for i in s1:
        if i not in s2:
            return False
        return True
    

if panagram(string1):
    print("it is a numerical panagram")
else:
    print("it is not a panagram")















