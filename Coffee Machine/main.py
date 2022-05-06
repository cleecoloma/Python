from pkg_resources import resource_isdir
from menu import MENU


end_coffee_machine = False
quarters = 0
dimes = 0
nickles = 0
pennies = 0
money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Check resources sufficient?
def resources_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
            
    
#Process Coins.
def calculate(quarters, dimes, nickles, pennies, price):
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    subtotal = (quarters/4) + (dimes/10) + (nickles/20) + (pennies/100)
    if subtotal > price:
        total = subtotal - price
        rounded_total = round(total, 2)
        print(f"Here is ${rounded_total} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")   
        
        
#Check transaction successful?
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕. Enjoy!")
      
      

#Prompt user by asking "What would you like? espresso/latte/cappuccino):"
while not end_coffee_machine:
    choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    #Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        end_coffee_machine = True
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${money}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            price = float(drink['cost'])
            is_successful = calculate(quarters, dimes, nickles, pennies, price)
            if is_successful:
                money += price
                make_coffee(choice, drink["ingredients"])

            