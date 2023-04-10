from random import randint

playing = True 
winning_streak = 0
grand_prize_streak = 3

while playing:
    coin_face = randint(1, 2)
    user_choice = int(input("Heads (1) or tails (2)? "))
    print(f"The random number is {coin_face}.")
    if user_choice == coin_face:
        print("That means your correct!")
        winning_streak += 1
        if winning_streak > 1:
            print(f"You're on a x{winning_streak} winning streak!")
    else:
        print("That means your sadly wrong ):")
        playing = False
if grand_prize_streak == winning_streak:
    print("Congrates, you won 3 times! Here's a website: https://binarypiano.com")
elif grand_prize_streak == winning_streak - 1:
    print("You were very close! If I could give $50, I might.")
else:
    print("Wow you suck.")