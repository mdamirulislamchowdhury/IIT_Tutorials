print("Welcome to the Python Coffee Shop!")

# Prices
price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50

# Ask for customer name
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

# Ask if customer is a student
student_status = input("Are you a student? (yes/no): ").lower()

# Initialize total bill
grand_total = 0

# Ordering loop
while True:
    print("\nMenu:")
    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_mocha))

    choice = input("What would you like to order? (coffee/latte/mocha): ").lower()

    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        cost = 0

    if cost > 0:
        quantity = int(input("How many cups would you like? "))
        total_cost = cost * quantity

        # Discount for multiple cups
        if quantity > 1:
            print("You get a discount of $1.00!")
            total_cost -= 1.00

        # Add to running total
        grand_total += total_cost
        print("Subtotal for this order: $" + str(round(total_cost, 2)))

    # Ask if customer wants to order more
    another = input("Would you like to order another drink? (yes/no): ").lower()
    if another != "yes":
        break

# Apply student discount
if student_status == "yes":
    print("You get a 10% student discount!")
    grand_total *= 0.90

print("\nYour final total is: $" + str(round(grand_total, 2)))
print("Thank you, " + customer_name + "! Please come again.")
