# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Display a menu for the user to choose an operation
print("Select a operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice
choice = input("Enter the number corresponding to the desired operation: ")

# Perform the selected operation and display the result
if choice == "1":
    result = num1 + num2
    operation = "Addition"
elif choice == "2":
    result = num1 - num2
    operation = "Subtraction"
elif choice == "3":
    result = num1 * num2
    operation = "Multiplication"
elif choice == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        operation = "Division"
else:
    print("Invalid choice. Please select a valid operation.")

# Print the result if a valid choice was made
if choice in ("1", "2", "3", "4"):
    print(f"{operation} result:", result)