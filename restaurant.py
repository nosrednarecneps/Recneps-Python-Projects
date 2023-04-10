print("Welcome to Lights-To-Eat")

i1 = "lamps"
i2 = "bulbs"

i1_price = 156.50
i2_price = 31.25

order_total = f'''
{"-" * 20}

Items
 - Price for {i1}: ${i1_price}
 - Price for {i2}: ${i2_price}
 
{"-" * 20}
'''
print(order_total)

buy_i1 = int(input(f"How many {i1} would you like to eat?: "))
buy_i2 = int(input(f"How many {i2} would you like to eat?: "))

i1_order = float(buy_i1 * i1_price)
i2_order = float(buy_i2 * i2_price)

order_total = f'''
{"-" * 20}

Order Summary
 - {buy_i1} {i1}
 - {buy_i2} {i2}
 
Order Prices
 - Price for {i1} order: ${i1_order}
 - Price for {i2} order: ${i2_order}
 
{"-" * 20}
'''
print(order_total)