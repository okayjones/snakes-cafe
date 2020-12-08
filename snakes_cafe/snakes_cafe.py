# Variables
quit_command = "quit"

menu = [
    # appetizers
    "wings",
    "cookies",
    "spring rolls",
    # entrees
    "salmon",
    "steak",
    "meat tornado",
    "a literal garden",
    # desserts
    "ice cream",
    "cake",
    "pie",
    # drinks
    "coffee",
    "tea",
    "unicorn tears",
]

order = {}

order_prompt = "> "

welcome = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""

# Helpers
def print_complete_order():
    print(
        """***********************************
Current Order:
  """
    )
    for (item, qty) in order.items():
        print(qty, item.title())
    print("***********************************\n")


def print_order(qty, item):
    if qty > 1:
        print(
            "\n** {} orders of {} has been added to your meal **\n".format(
                order[item], item.title()
            )
        )
    else:
        print(
            "\n** 1 order of {} has been added to your meal **\n".format(item.title())
        )


def take_order():
    # Order prompt
    item = input(order_prompt).strip().lower()

    if item == quit_command:
        quit()
    elif item not in menu:
        print("\n Oops! That item isn't on the menu. Place a new order. \n")
        take_order()
    elif item in order:
        order[item] += 1
        print_order(order[item], item)
        print_complete_order()
        take_order()
    else:
        order[item] = 1
        print_order(order[item], item)
        print_complete_order()
        take_order()


# Run it!
print(welcome)
take_order()
