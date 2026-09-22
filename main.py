import random


game_number = random.randint(1, 10)
guess_count = 0

while True:
    guess = int(input("Guess a number 1-10: "))
    guess_count += 1

    if guess > game_number:
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else:
        print(f"It took you {guess_count} guesses.")
        if guess_count == 1:
            print("your cheating")
        elif guess_count <= 3:
            print("good job.")
        else:
            print("that is awful.")
        break