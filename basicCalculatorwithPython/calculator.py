def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "ERROR,You can not division by zero bro"


def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                number1 = float(input("Enter the first number: "))
                number2 = float(input("Enter the second number: "))

            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"The result is: {add(number1, number2)}")
            elif choice == '2':
                print(f"The result is: {substract(number1, number2)}")
            elif choice == '3':
                print(f"The result is: {multiply(number1, number2)}")
            elif choice == '4':
                result = divide(number1, number2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"The result is: {result}")
            else:
                print("Invalid input.")

            next_calculation = input("Do you want to make another calculation? (yes/no): ").strip().lower()
            if next_calculation != 'yes':
                print("See you laateeerr ! ")
                break


if __name__ == "__main__":
    main()
