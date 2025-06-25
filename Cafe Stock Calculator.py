# In this task we are creating a stock calculating code.
# Use a list and dictionaries to multiply stock quantities by item prices to get the total stock value.

# Creating a list for the menu.
Menu = ["Latte", "Espresso", "Tea", "Iced coffee"]

# Assigning stock amount (quantity in units) to menu items.
stock = {
    "Latte": 200.00,
    "Espresso": 250.00,
    "Tea": 150.00,
    "Iced coffee": 350.45
}

# Placing corresponding prices to the menu items.
price = {
    "Latte": 56,
    "Espresso": 49,
    "Tea": 25,
    "Iced coffee": 60
}

# Initializing the total stock value.
total_stock_value = 0

# Calculating the total stock value using multiplication.
for item in Menu:
    item_value = stock[item] * price[item]
    total_stock_value += item_value

# Printing the final stock value.
print(f"The total stock value is R{total_stock_value:.2f}")
