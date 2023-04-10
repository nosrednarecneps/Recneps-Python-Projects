from random import randint

tokens = 4
rounds = 0
loop = 1
max_num = 10

while tokens > 0 and loop == 1:
    print(f"You have {tokens} tokens left.")
    play = input("Would you like to play and use a token (y/n): ")
    if play == "n":
        loop -= 1
    else:
        tokens -= 1
        print(f"You now have {tokens} tokens.")
        number = [randint(1, max_num) for i in range(3)]
        print(f"| {number[0]} | {number[1]} | {number[2]} |")
        if number[0] == number[1] and number[0] == number[2]:
            tokens *= 2
            print(f"Your tokens has doubled! You now have {tokens} tokens!")
        elif (number[0] == number[1] or number[2]) is True or (number[1] == number[2]) is True:
            tokens += 2
            print(f"You earned 2 tokens! You now have {tokens} tokens!")
        else:
            print("No matches. Nice try!")
if tokens == 0:
    print("Sorry, you have no more tokens. Come back if you can!")
else:
    print("Have a good day!")