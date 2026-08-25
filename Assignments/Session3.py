# name = input("Enter your name: ")
# favorite_food = input("Enter your favorite food: ")
#
# print(f"Hello {name}, your favorite food is {favorite_food}!")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# print("Sum:", num1 + num2)
# print("Difference:", num1 - num2)
# print("Product:", num1 * num2)
# print("Quotient:", num1 / num2)

# price = float(input("Enter the price of the food item: "))
# quantity = int(input("Enter the quantity: "))
#
# total_bill = price * quantity
#
# print(f"Your total bill is ₹{total_bill:.2f}")


# followers = int(input("Enter your Instagram follower count: "))
# print("\n\tYou have {:,} followers".format(followers))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Error: Invalid operator.")
