from random import randint

max_num = 10
offset = 2
random_number = randint(1, max_num)
lucky_number = randint(1, max_num)
lower_bound = random_number - offset
upper_bound = random_number + offset
guess = int(input("Take a guess between 1-10: "))
if guess < 11 and guess > 0:
    print(f"Ah, {guess}. Quite interesting!")
    print(f"The random number is {random_number}.")
    print(f"The lucky number is {lucky_number}.")
    if guess == random_number or guess == lucky_number:
        print("That means your correct!")
        print("Nice!")
        print("As a prize, here's a website: https://puginarug.com")
    elif guess >= lower_bound and guess <= upper_bound:
        print("That means your wrong.")
        print("But you were so close to that random number!")
        print("So hey, at least check this website out: https://longdogechallenge.com")
    else:
        print("That means your wrong.")
        print("Bummer.")
else:
    print("That's an invalid response!")
    print(f"The random number is {random_number}")
