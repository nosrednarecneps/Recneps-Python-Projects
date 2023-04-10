def display_options():
    print("""Welcome to the Weight Converter App!
 - To convert from pounds to kilograms, type 'lbs'
 - To convert from kilograms to pounds, type 'kg'""")

def convert_weight(amount, option):
    if option == "lbs":
        return str(round(float(amount) * 0.45359237)) + "kg"
    elif option == "kg":
        return str(round(float(amount) / 0.45359237)) + "lbs"
    else:
        return "We had a problem..."
        
loop = True
options = True

while loop:
    if options is True:
        display_options()
    option = input("What is your option?: ")
    amount = input("How much would you like to convert?: ")
    conversion = convert_weight(amount, option)
    print(f"{amount}{option} -> {conversion}")
    continue_program = input("Would you like to continue (y/n)?: ")
    if continue_program == "n":
        loop = False
    else:
        options = False
print("Thanks for using our app!")