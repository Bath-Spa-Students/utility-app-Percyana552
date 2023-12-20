# make a list of items that  vending machine should display
items = {
    "drinks": [
        {'code': 1, 'name': 'pepsi', 'price': 8, 'stock': 10},
        {'code': 2, 'name': 'coca cola', 'price': 5, 'stock': 20},
        {'code': 3, 'name': 'Lacnor', 'price': 25, 'stock': 50},
        {'code': 4, 'name': 'Fruit cocktail', 'price': 30, 'stock': 13},
        {'code': 5, 'name': 'water', 'price': 1, 'stock': 100},
        {'code': 6, 'name': 'natural juice', 'price': 5, 'stock': 20},
        {'code':7,'name':'juice','price':4,'stock':10}
    ],
    "snacks": [
        {'code':8, 'name': 'pringles', 'price': 16, 'stock': 25},
        {'code':10 , 'name': 'chips', 'price': 7, 'stock': 17},
        {'code':9 , 'name': 'salted cashews', 'price': 25, 'stock': 16}
    ],
    "sweets": [
        {'code': 11, 'name': 'roll cake', 'price': 20, 'stock': 5},
        {'code': 12, 'name': 'cupcake', 'price': 3, 'stock': 4},
        {'code': 13, 'name': 'Donuts', 'price': 9, 'stock': 13},
        {'code': 14, 'name': 'Muffins', 'price': 17, 'stock': 10},
        {'code': 16, 'name': 'cookies', 'price': 2, 'stock': 10},
        {'code': 17, 'name': 'cake', 'price': 10, 'stock': 15}
    ],
      "coffee": [
        {'code': 18, 'name': 'Espresso', 'price': 11, 'stock': 12},
        {'code': 19, 'name': 'Latte', 'price': 19, 'stock': 11},
        {'code': 20, 'name': 'cappuccino', 'price': 5, 'stock': 13},
        {'code': 21, 'name': 'Americano', 'price': 14, 'stock': 2}
    ] 
    }
print("Welcome to Petra's vending machine")
for category, category_items in items.items():
    print(category)
    for item in category_items:
        print(f"Code: {item['code']}, Name: {item['name']}, Price: {item['price']}, Stock: {item['stock']}")

user_item_code =int(input("Enter code (Enter 0 to Exit or 00 to add more items:)")) 

# here we are going to write vending machine code.
num_vending_machine=2
while user_item_code != 0:
    item = None
    for category in items.values():
        for i in category:
            if user_item_code == i['code']:
                item = i
                break
        if item:
            break

    if item:
        if item['stock'] > 0:
            print(f"Wonderful, {item['name']} will cost you {item['price']} AED, stock left: {item['stock']}")
            payment_method = input("Enter 2  if you would love to pay by cash or 3 if would like to pay by credit card: ")
            if payment_method == 3:
                print(" executing  credit  trasction ...")
                # here you would add credit card password
                print(" your payment is sucessful!")
            else:
                user_money = int(input(f"Enter {item['price']} AED to buy : "))
                while user_money < item['price']:
                    print("You don't have enough money for purchase this item.")
                    add_money = int(input(f"Please enter to add more money {item['price']-user_money} AED that you would like to Purchase: "))
                    user_money += add_money
                change = user_money - item['price']
                item['stock'] -= 1
                print(f"Thank you for purchase here is your {item['name']}. Stock left:{item['stock']},your change is {change}")
        else:
            print("Sorry, this item is out of stock.")
    else:
        print("The item code you entered doesn't exist.")
    print("\n another item you would like to buy:")
    for category, category_items in items.items():
        for item in category_items:
            print(f"Code: {item['code']}, Name: {item['name']}, Price: {item['price']}, Stock: {item['stock']}")
            print(f"\n There are (num_vending_machine) vending machine available.")
user_item_code = int(input("Enter code (Enter 0 to Exit or 00 to add more items:)"))
    
#  first you should make list in a way to give output the suggestios to the user.

suggestions = {
    1: "cookies",
    2: "Donuts",
    3: "pringles",
    4: "chips",
    5: "salted cashews",
    6: "chips",
    7: "cake",
    8: "pepsi",
    9: "coca-cola",
    10: "Lacnor",
    11: "Fruit cocktail",
    12: "water",
    13: "natural juice",
    14: "juice",
    15: "Latte",
    16: "Espresso",
    18: "Muffins",
    19: "roll cake",
    20: "cupcake",
    21: "Muffins"
}

# my vending machine suggestions-code.
if item:
    suggestion = suggestions.get(item['code'])
    if suggestion:
        print(f"\n I would recommend {suggestion} to go with your {item['name']}")
        