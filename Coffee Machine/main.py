from pkg_resources import resource_isdir
from menu import MENU


end_coffee_machine = False
quarters = 0
dimes = 0
nickles = 0
pennies = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#Check resources sufficient?
def drink_espresso():
    if int(resources['water']) > int(MENU['espresso']['ingredients']['water']) and int(resources['coffee']) > int(MENU['espresso']['ingredients']['coffee']):
        return True
def drink_latte():
    if int(resources['water']) > int(MENU['latte']['ingredients']['water']) and int(resources['milk']) > int(MENU['latte']['ingredients']['milk']) and int(resources['coffee']) > int(MENU['latte']['ingredients']['coffee']):
        return True   
def drink_cappuccino():
    if int(resources['water']) > int(MENU['cappuccino']['ingredients']['water']) and int(resources['milk']) > int(MENU['cappuccino']['ingredients']['milk']) and int(resources['coffee']) > int(MENU['cappuccino']['ingredients']['coffee']):
        return True
            
            
#Add money.
def cost_espresso():
    money += price
def cost_latte():
    money += price
def cost_cappuccino():
    money += price
    
    
#Process Coins.
def calculate(quarters, dimes, nickles, pennies, price):
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    subtotal = (quarters/4) + (dimes/10) + (nickles/20) + (pennies/100)
    if subtotal > price:
        total = subtotal - price
        rounded_total = round(total, 1)
        print(f"Here is ${rounded_total} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")   
        
        
#Check transaction successful?
def subract_espresso_resources():
    resources['water'] -= 50
    resources['coffee'] -= 18
def subract_latte_resources():
    resources['water'] -= 200
    resources['milk'] -= 150
    resources['coffee'] -= 24
def subract_cappuccino_resources():
    resources['water'] -= 250
    resources['milk'] -= 100
    resources['coffee'] -= 24    
      
      
money = 0
#Prompt user by asking "What would you like? espresso/latte/cappuccino):"
while not end_coffee_machine:
    choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    #Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        end_coffee_machine = True
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${money}")
    elif choice == "espresso":
        if drink_espresso != True:
            price = float(MENU['espresso']['cost'])
            is_successful = calculate(quarters, dimes, nickles, pennies, price)
            if is_successful:
                money += price
                # print(MENU['espresso']['cost'])
                resources['water'] -= 50
                resources['coffee'] -= 18
                print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Sorry, there is not enough water.")
    elif choice == "latte":
        if drink_latte == True:
            price = float(MENU['latte']['cost'])
            is_successful = calculate(quarters, dimes, nickles, pennies, price)
            if is_successful:
                money += price
                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
                print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Sorry, there is not enough water.")
    elif choice == "cappuccino":
        if drink_cappuccino == True:
            price = float(MENU['cappuccino']['cost'])
            is_successful = calculate(quarters, dimes, nickles, pennies, price)
            if is_successful:
                money += price
                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24   
                print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Sorry, there is not enough water.")
    else:
        print("Invalid input. Goodbye.")    