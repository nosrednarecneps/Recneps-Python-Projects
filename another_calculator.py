def calculate(num1, num2, operation):
    one_is_num = num1.isnumeric()
    two_is_num = num2.isnumeric()
    if ((one_is_num is True) and (two_is_num is True)) is True:
        num1 = float(num1)
        num2 = float(num2)
    else:
        return False
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "/":
        return str(num1 / num2)
    else:
        return False

loop = True
  
while loop:
    num1 = input("Please enter your first number: ")
    operation = input("Please enter your arithmetic operation (+, -, *, /,): ")
    num2 = input("Please enter your second number: ")
    answer = calculate(num1, num2, operation)
    if answer is False:
        print("We had an error...")
    else:
        print(f"{num1} {operation} {num2} = {answer}")
    continue_program = input("Would you like to perform another calculation (y/n)?: ")
    if continue_program == "n":
        loop = False
print("Thank you for using our calculator!")