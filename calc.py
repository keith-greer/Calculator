num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2

print("Addition result:", addition_result)
print("Subtraction result:", subtraction_result)
print("Multiplication result", multiplication_result)
print("Division result", division_result)
print("finish") 

print("\nChoose whether you want to add, subtract, multiply ir divide your numbers: ")
for i, location in enumerate(character_styles, start=1):
    print(f"{i}. {location}")
