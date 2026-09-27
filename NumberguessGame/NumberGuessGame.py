import random

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your number:"))
    if guess == number:
        print("Correct")
        break

    elif guess > number:
        print("Too High!")

    else:
        print("Too Low!")



