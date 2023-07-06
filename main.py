from data import MENU, resources
running = True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Money: ${:0,.2f}".format(resources['money']))


def resource_check(drink):
    drink_water_cost = drink["ingredients"]["water"]
    drink_milk_cost = drink["ingredients"]["milk"]
    drink_coffee_cost = drink["ingredients"]["coffee"]

    if drink_water_cost > resources['water']:
        print("Sorry there is not enough water.")
        return False
    elif drink_milk_cost > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    elif drink_coffee_cost > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        # resources['water'] -= drink_water_cost
        # resources['milk'] -= drink_milk_cost
        # resources['coffee'] -= drink_coffee_cost
        return True

def make_drink(drink):
    drink_water_cost = drink["ingredients"]["water"]
    drink_milk_cost = drink["ingredients"]["milk"]
    drink_coffee_cost = drink["ingredients"]["coffee"]

    resources['water'] -= drink_water_cost
    resources['milk'] -= drink_milk_cost
    resources['coffee'] -= drink_coffee_cost


while running == True:
    #TODO: 1 Ask if the user wants an espresso/latte/cappuccino
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    #TODO: 1.1 Check user input to decide what to do next
    #TODO: Turn the coffee machine off by typing "off"
    if choice == "off":
        running = False
    #TODO: 3 Print a report of all of the resources. (This includes the money in the machine)
    elif choice == "report":
        report()
    #TODO: 4 Check if the resources in the machine are enough to make the drink - if any 1 is out print "Sorry there is not enough resources"
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        enough_resource = resource_check(MENU[choice])
    #TODO: 5 Process coins. If there are enough resources to make the drink, ask user for coins. Quarters, Dimes, Nickles, Pennies.
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        #TODO: 6 Calculate the monetary value of the coins
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        ## print("${:0,.2f}".format(total))
        #TODO: 7 Check if the transaction is successful
        #TODO: 7.1 If not enough money let user know and refund money.
        if total < MENU[choice]["cost"]:
            print("Sorry that's not enough money")
        #TODO: 7.2 If there is enough money the cost of the drink gets added to the machine as profit
        # TODO: 7.3 If the user entered too much money, machine offers change.
        else:
            change = total - MENU[choice]["cost"]
            resources["money"] += MENU[choice]["cost"]
            print("Here is ${:0,.2f} in change".format(change))

        #TODO: 8 Make the coffee if the transaction is successful, and the ingredients should be deducted from the coffee machine resources.
            make_drink(MENU[choice])
            print(f"Here is your {choice}, enjoy!")
        #TODO: 9 Tell the user: "Here is your {drink}. Enjoy!"


    else:
        print("That is not a valid choice.")