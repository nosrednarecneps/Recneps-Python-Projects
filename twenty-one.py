from random import randint
from time import sleep

min_cards = 1
max_cards = 20
max_card = 10
player_cards = randint(min_cards, max_cards)
dealer_cards = randint(min_cards, max_cards)

print("Welcome to Twenty One!")
sleep(1)
print("Drawing cards!")
sleep(2)
print(f"You have {player_cards}!")
hit = int(input("Would you like to hit(1) or stand(0): "))
if hit == 1:
    player_cards = player_cards + randint(1, max_card)
    print(f"You now have {player_cards}!")
print(f"The dealer has {dealer_cards}!")
if player_cards > 21 or dealer_cards > player_cards:
    print("Yeah sorry, you lost that one.")
    if player_cards > 21:
        print("I guess your too swole for this game.")
else:
    print("Nice! You won!")