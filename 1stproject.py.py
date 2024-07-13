menu={
    'pizza':40,
    'pasta':50,
    'burger':40,
    'coffee':40,
    'salad':70,
    }
print("welcome to python menu card")
print("pizza: rs40\npasta: rs50\nburger: rs50\ncoffee: rs50\nsalad: rs50")
order_total=0



item_1=input("What is your first item? ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Sorry {item_1} is not available")
another_order=input("do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("What is your second item? ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Sorry {item_2} is not available")
print(f"the total amount of items to pay is{order_total}")
