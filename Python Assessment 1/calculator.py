def calculator():
    print("Please type in the math operation you would like to complete:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    operation = input()

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")

    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")

    elif operation == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("UNDIFINED: Division by zero is not possible.")

    else:
        print("Invalid operator")

    again() #calling function to ask if the user wants to calculate again


def again():
    print("Do you want to calculate again?")
    print("Type Y for yes or N for no.")
    calc_again = input()

    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print()
    else:
        again()

calculator()