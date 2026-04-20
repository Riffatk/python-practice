import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct! The number is", secret)
        break
    elif guess < secret:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
