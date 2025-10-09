#pangram checker 
#first approach(not complete)
string1  = input("Type up your sentence!")
vowels = {"a":0, "e":0,"i":0,"o":0,"u":0}
for i in string1:
    if i in vowels:
        vowels[i] = vowels[i] +1
print(vowels)

#second approach
string1 = input("Type your sentence")
char_count = {}
for i in string1:
    if i isalpha():
        if i in char_count:
            char_count[i] = char_count[i] +1
        else:
            char_count = 1
print(char_count)

