import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Number is too low.")
        elif guess > random_number:
            print("Sorry, guess again. Number too high.")

    print(f"Congrats, You got it right...You have guessed number {random_number}.")

# guess(10)


def computer_guess(x):
    guess = 0

    while guess != x:
        guess = random.randint(1, x+1)
        print("Keep trying...")

    print(f"Congrats...You nailed it. Guess number is {x}.")

def computer_guess_improved_version(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)

        else:
            guess = low # could also be high as we know low=high
        feedback = input(f"Is {guess} too High (H), too low (L) or correct (C).")
        if feedback == 'h':
            high = guess + 1
        elif feedback == "l":
            low = guess + 1

    print(f"Congrats! Computer guessed it right and number is, {guess}.")

computer_guess(10)

print("Calling improved version of guess function.................")
computer_guess_improved_version(100)

