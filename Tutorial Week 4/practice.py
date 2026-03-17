'''# Step 1:
print("Welcome to the Python Coffee Shop!")

# Step 2:
customer_name = input("What is your name?")
print("Hello," + customer_name + "! Let's order some coffee.")

# Step 3:
price_coffee = 3.50
price_latte = 4.00

print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))

# Step 4:
menu_items = ["coffee", "latte", "espresso"]
print("Our menu:", menu_items) '''

# Step 5:
print("Welcome to the Python Coffee Shop!")

#asking user input
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50

Gtotal = 0
order = True

while order:
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
        continue

    quantity = int(input("How many cups would you like? "))
    total_cost = cost * quantity

    if quantity > 1:
        print("You get a discount of $1.00!")
        total_cost -= 1.00

    Gtotal += total_cost

    again = input("Would you like to order again? (yes/no):").lower()
    if again == "no":
        order = False

student = input("Are you a student? (yes/no): ").lower()
if student == "yes":
    discount = Gtotal * 0.10
    Gtotal -= discount
    print("Student discount applied (10% off)!")

print("Your total is: $" + str(round(Gtotal,2)))

print("Thank you, " + customer_name + "! Please come again.")

