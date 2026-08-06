

# part 1 star pyramid pattern
print("====== Star Pyramid Pattern ======")

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()


# part 2 Floyd's triangle pattern
print("====== Floyd's Triangle Pattern ======")


number = 1

rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print(number, end=" ")
        number += 1
    print()


# part 3 Diamond number pattern
print("====== Diamond Number Pattern ======")

rows = int(input("Enter the number of rows: "))

# Upper half
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print(k + 1, end="")
    print()

# Lower half
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print(k + 1, end="")
    print()
# part 4 final message
print("====== Pattern Printing Completed ======")
