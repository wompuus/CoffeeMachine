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
        return True


def make_drink(drink):
    drink_water_cost = drink["ingredients"]["water"]
    drink_milk_cost = drink["ingredients"]["milk"]
    drink_coffee_cost = drink["ingredients"]["coffee"]

    resources['water'] -= drink_water_cost
    resources['milk'] -= drink_milk_cost
    resources['coffee'] -= drink_coffee_cost


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


while running:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        running = False

    elif choice == "report":
        report()

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        enough_resource = resource_check(MENU[choice])
        total = process_coins()

        if total < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")

        else:
            change = total - MENU[choice]["cost"]
            resources["money"] += MENU[choice]["cost"]
            print("Here is ${:0,.2f} in change".format(change))

            make_drink(MENU[choice])
            print(f"Here is your {choice}, enjoy!")

    else:
        print("That is not a valid choice.")
