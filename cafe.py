# In this task we are creating a stock calculating code.
# Use List and Keys and multiply the values to  get final stock value.

# Creating a list for menu.

Menu = ["Latte" , "Espresso" , "Tea" , "Iced coffee"]

# Assigning stock amount to menu.

stock = {"Latte": 200.00,
         
        "Espresso": 250.00 ,
         
        "Tea": 150.00 ,
           
        "Iced coffee": 350.45}

# Placing corresponding price to the menu.

price = {"Latte" : 56 ,
         
         "Espresso" : 49 , 
         
         "Tea" : 25 ,
          
         "Iced coffee" : 60 }

# Setting conditions to calculate the required total Stock value in Rands.

for items in Menu:

    total_stock = stock[items]

    total_price = price[items]

    # Calculating the total stock value using multiplication.

    tota_value = total_stock * total_price

# Printing the final stock value.

print(f"The total stock value is R{total_stock:.2f}")
