import random

r_no = random.randint(1,10)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < r_no:
            print("Too low")
        elif guess > r_no:
            print("Too high")
        else:
            print("You guessed it!")
            break

    except ValueError:
        print("That is not a number.")
