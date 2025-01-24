# Ifa Namee
# 1/22/2025
# North loop Provisions - Donut shop Management stytem
# Your first python program for module 2

import time

def welcome_message():
    # Display a welcome message
    print("....................................................")
    print()
    print("Welcome to Loop Provisions!")
    print("Crafting artisinal donuts in Minneapolis' North Loop")
    print()
    print("....................................................")

def show_menu():
    """Display our current donut menu."""
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "MN Berry": 4.25,
        "Local Honey": 4.00
    }

    print("\nToday's Donut Menu: ")
    print()
    for donut, price in menu.items():
        print(f"    {donut}: ${price:.2f}")
    print()
    

# Main program
if __name__== "__main__":
    welcome_message()
    show_menu()
    print("......................................................")
    print("\nReady to serve our community with the finest donuts!")

    # Print current date and time this program open or now 
    current_time = time.localtime()
    formatted = time.strftime("%m-%d-%Y, %I:%M %p", current_time)
    print("Current date and time:", formatted)
    print()
    print("......................................................")
    print()

# Our complete menu organized by category
donut_menu = { # dictionary with key-value pairs where the value is list.
    'Small Batch': [
        'Wild Rice & Honey',
        'Maple Bacon',
        'Swedish Cardamom'
    ],
    'Seasonal': [
        'Apple Cider',
        'Jucy Lucy',
        'Lake of the Woods'
        ],
    'Local Collabs': [
        'Spyhouse Coffee Cake',
        'Fulton Beer & Pretzel',
        'Sweet Science Ice Cream'
        ]
    }

# Locally-sourced toppings
toppings = [
    'House-made Sprinkles',
    'Candied Hazelnuts',
    'Bee Pollen',
    'Cookie Butter Drizzle'
]

# Track our morning sales with a dictionary
morning_sales = []

# Record our first sale (by appending a transaction to the sales dictionary)
morning_sales.append({
    'item': 'Wild Rice & Honey',
    'quantity': 2,
    'toppings': ['Bee Pollen'],
    'time': '7:30 AM'
})

morning_sales.append({
    'item': 'Swedish Cardamom',
    'quantity': 1,
    'toppings': ['Cookie Butter Drizzle'],
    'time': '8:00 AM'
})

# Display our current menu - using a for loop 
print("     Todays Morning Menu: ")
print()
for category, items in donut_menu.items():
    print("    ", category + ":")
    for item in items:
        print("         - " + item)

print()
total_quantity = 0  # Variable to intalize total quantity.

# Print morning sales with list of items by using for loop and 
# type to Check if the value is a list
print("......................................................")
print()
print("    Morning sale list is here: ")
print()
for sale in morning_sales:
    for item, value in sale.items():
        if type(value) == list: # or if isinstance(value, list):
            print(f"    - {item}: {', '.join(value)}")
        else:
            print(f"    - {item}: {value}")
            

    # To count how many quantity sold 
    total_quantity += sale['quantity']
    print() 

print("......................................................")
print()
print(f"Total quantity sold: {total_quantity}")
print()
print("......................................................")
    