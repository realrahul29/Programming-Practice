print("PATTERN 1")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPATTERN 2")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()

print("\nPATTERN 3")
letters = "python"
for i in range(len(letters)):
    print(letters[i] * (i + 1))

print("\nPATTERN 4")
word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])
