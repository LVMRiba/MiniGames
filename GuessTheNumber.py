from random import randint
import time

##### GUESS THE NUMBER: YOU VERSION
def you_vs_pc():
    number = randint(0, 99)
    guess = -1
    tries = 0

    while number != guess:
        tries += 1
        print(5 * "=" + f" TENTATIVA {tries} " + "=" * 5)
        guess = int(input('CHOOSE A NUMBER: '))
        if guess > number:
            print("Number > Guess")
        elif guess < number:
            print("Guess < Number")
        else:
            print(f"PARABÉNS!\nO NÚMERO ERA: {number}")


##### GUESS THE NUMBER: PC VERSION
def pc_vs_you():
    number = int(input('CHOOSE A NUMBER: '))
    number_low = 0
    number_high = 99
    guess = -1
    tries = 0

    while number != guess:
        tries += 1
        print(5 * "=" + f" TENTATIVA {tries} " + "=" * 5)
        guess = randint(number_low, number_high)
        print(f"GUESS: {guess}")
        if guess > number:
            number_high = guess - 1
        elif guess < number:
            number_low = guess + 1
        else:
            print(f"GANHEI!\nO NÚMERO ERA: {number}")
        if number_low != number_high:
            print(f"O Número está entre {number_low} e {number_high}")
        time.sleep(2)

you_vs_pc()
pc_vs_you()