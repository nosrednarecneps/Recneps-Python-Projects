welcome_banner = """Welcome to the List Workout!
    In this app, you'll need to create lists based off of
    the prompts below and display the correct item from 
    each list to answer the prompt.
"""
print(welcome_banner)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)
print(f"There are {len(planets)} planets!")
print(f"We live on planet {planets[2]}.")
print(f"The closest planet to the sun is {planets[0]}.")
print(f"The farthest planet from the sun is {planets[7]}.")
print(f"The great red spot is on {planets[4]}.")
random_planet = 'Pluto'
print(f"Is {random_planet} in our planets list?")
planets.append(random_planet)
set_list = sorted(list(set(planets)))
sorted_list = sorted(planets)
if set_list != sorted_list:
    planets.pop(-1)
    print(f"Yes, {random_planet} is in our list!")
else:
    planets.pop(-1)
    print(f"No, {random_planet} isn't in our list!")
    print(f"Let's add {random_planet} to our list of planets.")
    planets.append(random_planet)
    if planets[-1] != random_planet:
        print(f"{random_planet} has not been added to the planets list.")
    else:
        print(f"{random_planet} has been added to the planets list.")
        print("Nevermind, let's remove Pluto from the list of planets.")
        subtracted = planets.pop(-1)
        planets.pop(-1)
        if planets[-1] != subtracted:
            print(f"{random_planet} has been removed from the planets list.")
        else:
            print(f"{random_planet} is still in the planets list.")