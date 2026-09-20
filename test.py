#step 1
def test_2(a, b):
    return a + b
def test_3(a, b):
    return a - b
def test_4(a, b):
    return a * b
def test_5(a, b):
    return a / b
#step 2
try:
    print(float(input("Enter a number: ")))
except ValueError:
    print("Invalid input. Please enter a valid number.")
