#1
print (458 + 751)

#2
print ("How are you?")

#3
print(8 / 3, 4 * 7, 9 + 13, 2 ** 5, 6 * (3 + 2))

#4
size = 77

#5
x = 5
y = 7
print(abs(x - y) - 10)
print(int(x ** 2) + 1.4)
print(round(y + 3.14159, 2))

#6
a = 31
b = 7
print(a // b, a % b)

#7
t_m= 250
h = t_m // 60
m = t_m % 60

print("Hours:", h)
print("Minutes:", m)

#8
str1 = "it is what it is"
print(str1.find("is"), str1.rfind("it"), str1[-9:-7])

#9
str1 = "it is what it is"
print(str1[-9:])

#27
a = 2
b = 3
c = 7

if (a * b) < c:
    b = a
else:
    c = a + b + c

print(a, b, c)

#28
# Assume the response is B
letter = input("Enter A, B, or C: ")
letter = letter.upper()

if letter == "A":
    print("A, my name is Alice.")
elif letter == "B":
    print("To be, or not to be.")
elif letter == "C":
    print("Oh, say, can you see.")
else:
    print("You did not enter a valid letter.")

#29
isvowel = False
letter = input("Enter a letter: ")
letter = letter.upper()

if letter in "AEIOU":
    isvowel = True

if isvowel:
    print(letter, "is a vowel.")
elif not (65 <= ord(letter) <= 90):
    print("You did not enter a letter")
else:
    print(letter, "is a consonant.")
