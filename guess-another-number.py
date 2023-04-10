from random import randint

min_num = 1
max_num = 3
playing = True
rounds = 0
win = False
number = randint(min_num, max_num)

while playing:
    rounds += 1
    guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
    if guess == number:
        print("You got it right!")
        win = True
        playing = False
    elif guess not in range(min_num, (max_num + 1)):
        print("That was way off!")
    elif guess < number:
        print("Ouch, you were just under!")
    else:
        print("Darn, you were over a little!")
    if win is False:
        keep_on = input("Would you like to play another round (y/n): ")
        if keep_on == "n":
            playing = False
        else:
            print("Alright!")
if win is True:
    if rounds == 1:
        print("Congrats! You won your first try!")
    else:
        print(f"Congrats! You won in {rounds} rounds!")
else:
    print("Nice try!")