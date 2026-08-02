string=input("Enter a string: ")
char=input("Enter a character to search for: ")
count=0
i=0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print(f"The character '{char}' appears {count} times in the string.")
