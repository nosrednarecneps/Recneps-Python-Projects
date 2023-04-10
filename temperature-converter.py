def display_options():
    options = """
Welcome to the Temperature Converter App
Conversion Options
    (f) Fahrenheit to Celsius
    (c) Celsius to Fahrenheit
"""
    print(options)

def display_results(temp, typ):
    if typ == "f":
        new_temp = (input_temp - 32) * (5/9)
        new_typ = "c"
    else:
        new_temp = (input_temp * (9/5)) + 32
        new_typ = "f"   
    print("{:.1f}".format(temp) + f"°{typ}" + "  ->  " + "{:.1f}".format(new_temp) + f"°{new_typ}")

while True:
    display_options()
    option = input("Please input a valid option: ")
    input_temp = float(input("Enter input temperature: "))
    display_results(input_temp, option)
    keep_converting = input("Would you like to convert another temperature? (y/n) ")
    if keep_converting != "y":
        break

print("Thanks for using the app!")