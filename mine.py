guess=int(input("Enter your guess: "))
while guess != 7:
    if guess < 7:
        print("Too low!")
    elif guess > 7:
        print("Too high!")
    else:
        print("You guessed it!")
