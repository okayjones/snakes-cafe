# Variables
quit_command = 'Quit'

menu = [
  #appetizers
  "Wings", "Cookies", "Spring Rolls",
  #entrees
  "Salmon", "Steak", "Meat Tornado", "A Literal Garden",
  #desserts
  "Ice Cream", "Cake", "Pie",
  #drinks
  "Coffee", "Tea", "Unicorn Tears"
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
  print("""***********************************
Current Order:
  """)
  for key in order:
    print(order[key], key)
  print("***********************************\n")

def print_order(qty, item):
  if qty > 1:
    print('\n** {} orders of {} has been added to your meal **\n'.format(order[item], item))
  else:
    print('\n** 1 order of {} has been added to your meal **\n'.format(item))

def take_order():
  # Order prompt
  item = input(order_prompt).title()

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
