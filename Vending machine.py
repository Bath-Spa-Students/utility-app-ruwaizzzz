########################################################################################################################################
#                                                          VENDING MACHINE!!!                                                          #
########################################################################################################################################
items = {
    '1': {'name': 'Chips', 'price': 3.00},
    '2': {'name': 'Cola', 'price': 4.00},
    '3': {'name': 'Water', 'price': 2.00},
    '4': {'name': 'Chicken Burger', 'price': 8.00},
    '5': {'name': 'Juice', 'price': 3.00},
    '6': {'name': 'Chocolate Bar', 'price': 3.00}
}
print("*Power On*\n")
print(f"\tWelcome to the Eat And Drink Vending Machine")
print(f"\tPlease purchase any of our wares:")
print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


for key, item in items.items():
    print(f"{key}. {item['name']} - ${item['price']}")

object = input("Enter the item number you wish to purchase: ")

# Validation
if object in items:
    selected_item = items[object]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"You have selected {selected_item['name']}.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    amount_due = selected_item['price']

    # Money Stuff
    while amount_due > 0:
        try:
            payment = float(input(f"Please insert ${amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"You have successfully purchased {selected_item['name']}!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Thank you for your purchase! Your change is ${change:.2f}")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")