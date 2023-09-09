def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."


def calculator():
    while True:  # Loop until /exit is entered
        option = input("(+/-/x/÷): ")
        if option == "/exit":
            print("Exited")
            break
        num1 = float(input("Number 1: "))  # Convert input to float
        num2 = float(input("Number 2: "))  # Convert input to float

        if option == "+":
            result = add(num1, num2)
        elif option == "-":
            result = subtract(num1, num2)
        elif option == "x":
            result = multiply(num1, num2)
        elif option == "÷":
            result = divide(num1, num2)
        else:
            print("Invalid option.")
            continue  # Continue the loop for invalid options

        print("Result:", result)


if __name__ == "__main__":
    calculator()
