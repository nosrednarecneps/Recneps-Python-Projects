print('''Hola

-----
''')
score = 0
q1 = input("""Which is a lie!
    (1) Spencer played Valorant since day 1.
    (2) Spencer played Call of Duty Modern Warfare since day 1.
    Please input a number: """)
if q1 == '1':
    print("Unfortinately yes...")
    score = score + 1
elif q1 == '2':
    print("Unfortinately no...")
else:
    print("Dude, nada valid fool!")
q2 = str(input("""Which is a lie!
    (1) Spencer likes the male gender.
    (2) Spencer likes the female gender.
    Please input a number: """)) 
if q2 == '1' or q2 == '1':
    print("Trick question; both 😈")
    score = score + 1
else:
    print("You really threw this one...")
print('''
-----
''')
print(f"Your Score: {score}")
if score > 1:
    print("You know who you are? Your the GOAT!")
elif score == 1:
    print("I mean it's all right |:")
else:
    print("-_-")
