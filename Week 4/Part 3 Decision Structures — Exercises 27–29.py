a = 2
b = 3
c = 7

if (a * b) < c:   # 2*3 = 6 < 7 → True
    b = a         # b = 2
else:
    c = a + b + c

print(a, b, c)







# Assume the response is B
letter = input("Enter A, B, or C: ")   # B
letter = letter.upper()                # still "B"

if letter == "A":
    print("A, my name is Alice.")
elif letter == "B":
    print("To be, or not to be.")
elif letter == "C":
    print("Oh, say, can you see.")
else:
    print("You did not enter a valid letter.")






isvowel = False
letter = input("Enter a letter: ")  # assume input "B"
letter = letter.upper()             # "B"

if letter in "AEIOU":   # "B" not in vowels
    isvowel = True

if isvowel:
    print(letter, "is a vowel.")
elif not (65 <= ord(letter) <= 90): # "B" ASCII = 66 → valid letter
    print("You did not enter a letter")
else:
    print(letter, "is a consonant.")
