print("Welcome to the Tip Calculator!")
order = float(input("What's the total amount of your order? "))
percentage = float(input("What percent do you want to tip? "))
tip = (percentage / 100) * order
total = order + tip
print("You should tip $" + str(tip))
print("The total with tip is $" + str(total))
