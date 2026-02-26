string1 = input("Type your sentence")

def panagram(string1):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")#this specifically tells the computer that you are using a set
    c1 = set()


    for c in string1:
        if c.isalpha():
            c1.add(c.lower())

    for i in alphabet: #comparing the two sets to see if both are equal
        if i not in c1 :
            return False
    return True

if panagram(string1):
    print("is a panagram")
else:
    print("not a panagram")

#created two sets
#first one is used to contain all letters in the alphabet
#second one was empty so that we could add all the characters in the users sentence (string1) 
#then we checked if all letters in string1 are letters of the alphabet
#if all characters in string1 are letters then we add tem to c1
#next we compared the two sets, alphabet and c1
#if all the characters in c1 was not fully in alphabet then that meant it was not a panagram









