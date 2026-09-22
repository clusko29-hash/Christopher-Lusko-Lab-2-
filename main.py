import random


game_number = random.randint(1,10)
print(game_number)
while(True):
    guess = int(input("Guess a number 1-10: "))
    if guess > game_number:
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else:
        print("You Win")
        break