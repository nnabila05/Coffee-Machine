MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 3. print report



# Todo 5. Process coins
def process_coins():
    global total_amount
    quarters = float(input("Please, insert your coins. /n How many quarters? "))
    dimes = float(input("How many dimes?"))
    nickels = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_amount


global total_amount


# TODO 6. check transaction

global balance
def check_transaction(total_amount: object, user_choice: object,balance) -> object:
    if total_amount >= MENU[user_choice]['cost']:
        change = total_amount - MENU[user_choice]['cost']
        print(f"here's your ${round(change, 2)} change")
        balance += MENU[user_choice]["cost"]
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


# TODO 4. check if theres sufficient resources available


def check_resource(user_choice):
    """checks if there is enough resources left for the ordered coffee"""
    for item in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][item]> resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
        else:
            return True


# TODO 7. make coffee


def make_coffee(user_choice):
    """Deduct the items from resources """
    for item in MENU[user_choice]["ingredients"]:
        resources[item] -= MENU[user_choice]["ingredients"][item]

    print(f"Here's your {user_choice} ☕☕☕, enjoy!!")
    return resources


# TODO 1. asking user what they want

balance = 0
resources["money"] = balance
turn_on = True

while turn_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        turn_on = False
    elif user_choice == "report":
        print(resources)
    else:

        if check_resource(user_choice):
            process_coins()
            if check_transaction(total_amount, user_choice,balance):

                make_coffee(user_choice)
                balance += MENU[user_choice]["cost"]

                resources["money"] = balance

