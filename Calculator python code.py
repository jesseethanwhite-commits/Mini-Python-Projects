# Define functions for basic arithmetic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    # Handle division by zero error
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        # Get user input for operation choice
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                # Get numbers from the user and convert to float
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue # Restart the loop to ask for valid numbers

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break # Exit the while loop
        
        else:
            print("Invalid Input. Please enter a valid option.")

# Call the calculator function to start the program
calculator()
