import random
import utill


def main():
    utill.print_header('mm')
    print("Guess the number of M&Ms and you get lunch on the house!\n")
    loop()


def get_guess():
    guess_text = input("How many M&Ms are in the jar?\n ")
    guess = int(guess_text)
    return guess


def loop():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    while attempts < attempt_limit:
        guess = get_guess()
        attempts += 1

        if mm_count == guess:
            print(f"You got a free lunch! It was {guess}.")
            break
        elif guess < mm_count:
            print("Sorry, that's too LOW!")
        else:
            print("That's too HIGH!")

    print(f"Bye, you're done in {attempts} tries thire are {mm_count} mms!")


main()






