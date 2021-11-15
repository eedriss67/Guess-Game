# Guessing game project.
import random


# Computer to guess
secret_num = 230


def computer(x):
    num1 = 1
    num2 = x
    guesses = ""
    while guesses != "g":
        if num1 != num2:
            number = random.randint(num1, num2)
        else:
            number = num1
        guesses = input(f"{number} high (H), low (L), guessed (G) ".lower())
        if guesses == "h":
            num2 = number - 1
            print("guess is high")
        elif guesses == "l":
            num1 = number + 1
            print("guess is low")

    print(f"Yeah, the computer guessed the secret number: ({secret_num}) correctly.")


computer(500)


print()

# User to guess

secret_number = 35
guess_count = 0

while not secret_number or guess_count < 11:
    guess = int(input("Guess a number from 1 - 50: "))
    guess_count += 1

    if guess < secret_number:
        print("guess is low")
    elif guess > secret_number:
        print("guess is high")
    else:
        print(f"You have guessed the secret number, number {secret_number} correctly. Congrats!")
        break
