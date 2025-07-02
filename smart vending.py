import time
import random
import json
import os

# Multilingual support
LANG = "en"

# Load or initialize user loyalty data
LOYALTY_FILE = "loyalty_data.json"
if os.path.exists(LOYALTY_FILE):
    with open(LOYALTY_FILE, "r") as f:
        user_loyalty = json.load(f)
else:
    user_loyalty = {}

# Items database
items = {
    "Drinks": [
        {'code': 1, 'name': 'Pepsi', 'price': 8, 'stock': 10},
        {'code': 2, 'name': 'Coca Cola', 'price': 5, 'stock': 20},
        {'code': 3, 'name': 'Lacnor', 'price': 25, 'stock': 50},
        {'code': 4, 'name': 'Fruit Cocktail', 'price': 30, 'stock': 13},
        {'code': 5, 'name': 'Water', 'price': 1, 'stock': 100},
        {'code': 6, 'name': 'Natural Juice', 'price': 5, 'stock': 20},
        {'code': 7, 'name': 'Juice', 'price': 4, 'stock': 10}
    ],
    "Snacks": [
        {'code': 8, 'name': 'Pringles', 'price': 16, 'stock': 25},
        {'code': 9, 'name': 'Chips', 'price': 7, 'stock': 17},
        {'code': 10, 'name': 'Salted Cashews', 'price': 25, 'stock': 16}
    ],
    "Sweets": [
        {'code': 11, 'name': 'Roll Cake', 'price': 20, 'stock': 5},
        {'code': 12, 'name': 'Cupcake', 'price': 3, 'stock': 4},
        {'code': 13, 'name': 'Donuts', 'price': 9, 'stock': 13},
        {'code': 14, 'name': 'Muffins', 'price': 17, 'stock': 10},
        {'code': 15, 'name': 'Cookies', 'price': 2, 'stock': 10},
        {'code': 16, 'name': 'Cake', 'price': 10, 'stock': 15}
    ],
    "Coffee": [
        {'code': 17, 'name': 'Espresso', 'price': 11, 'stock': 12},
        {'code': 18, 'name': 'Latte', 'price': 19, 'stock': 11},
        {'code': 19, 'name': 'Cappuccino', 'price': 5, 'stock': 13},
        {'code': 20, 'name': 'Americano', 'price': 14, 'stock': 2}
    ]
}

suggestions = {
    1: "Cookies", 2: "Donuts", 3: "Pringles", 4: "Chips",
    5: "Salted Cashews", 6: "Chips", 7: "Cake", 8: "Pepsi",
    9: "Coca Cola", 10: "Lacnor", 11: "Fruit Cocktail",
    12: "Water", 13: "Natural Juice", 14: "Juice", 15: "Latte",
    16: "Espresso", 17: "Muffins", 18: "Roll Cake", 19: "Cupcake", 20: "Muffins"
}

total_earnings = 0
item_sales = {}

# Load/Save Loyalty
def save_loyalty_data():
    with open(LOYALTY_FILE, "w") as f:
        json.dump(user_loyalty, f)

def display_items():
    print("\n📦 Available Items")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for category, category_items in items.items():
        print(f"\n🔹 {category}")
        for item in category_items:
            low_stock = "⚠️ LOW STOCK!" if item['stock'] < 5 else ""
            print(f"  [{item['code']:02}] {item['name']:<16} - {item['price']} AED (Stock: {item['stock']}) {low_stock}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

def find_item_by_code(code):
    for category_items in items.values():
        for item in category_items:
            if item['code'] == code:
                return item
    return None

def find_item_by_name(name):
    for category_items in items.values():
        for item in category_items:
            if item['name'].lower() == name.lower():
                return item
    return None

def handle_payment(item):
    print("💰 Choose payment method:")
    print("   [1] Cash\n   [2] Credit Card\n   [3] Sensor\n   [4] Apple Pay\n   [5] Google Pay")

    while True:
        method = input("🔑 Enter method (1-5): ").strip()
        if method not in ['1', '2', '3', '4', '5']:
            print("❗ Invalid option. Try again.")
        else:
            break

    if method == '3':
        print("🖐️ Please scan your hand/eye...")
        time.sleep(2)
        print("✅ Sensor payment successful!")
    elif method in ['4', '5']:
        print("📱 Processing digital payment...")
        time.sleep(1.5)
        print("✅ Payment successful via", "Apple Pay" if method == '4' else "Google Pay")
    else:
        while True:
            try:
                user_money = int(input("💳 Enter amount (AED): "))
                break
            except ValueError:
                print("❗ Please enter a valid number.")
        while user_money < item['price']:
            print(f"⚠️ Not enough. You need {item['price'] - user_money} AED more.")
            try:
                more = int(input("➕ Add more AED: "))
                user_money += more
            except ValueError:
                print("❗ Please enter a valid number.")
        change = user_money - item['price']
        print(f"💸 Change: {change} AED")

    item['stock'] -= 1
    item_sales[item['name']] = item_sales.get(item['name'], 0) + 1
    print("\nProcessing order...", end="")
    time.sleep(1)
    print(" ✅ Done!")
    print(f"🎁 Enjoy your {item['name']}")
    print(f"📦 Remaining Stock: {item['stock']}")

def handle_suggestion(original_code):
    if original_code in suggestions:
        suggestion_name = suggestions[original_code]
        print(f"\n🍽 Suggested pairing: Would you like to try **{suggestion_name}**?")
        choice = input("👉 Type yes to continue or no to skip: ").strip().lower()
        if choice in ['yes', 'y']:
            suggested_item = find_item_by_name(suggestion_name)
            if suggested_item and suggested_item['stock'] > 0:
                print(f"\n🛍️ You selected: {suggested_item['name']} - {suggested_item['price']} AED")
                handle_payment(suggested_item)
                return suggested_item['price'], suggested_item['name']
            else:
                print(f"❌ Sorry, {suggestion_name} is out of stock.")
    return 0, None

def generate_qr_receipt(purchased_items, total_spent):
    print("\n📎 QR Code Receipt (simulated):")
    receipt_id = random.randint(100000, 999999)
    print(f"🧾 RECEIPT ID: #{receipt_id}")
    print("🛍 ITEMS:")
    for item in purchased_items:
        print(f" - {item}")
    print(f"💰 TOTAL: {total_spent} AED")
    print(f"🕒 Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📱 QR STRING: PETRA-{receipt_id}-{total_spent}-AED")
    print("📲 Scan in Petra App for loyalty points!\n")

def admin_dashboard():
    global total_earnings
    print("\n🛠️ Admin Dashboard (Authenticated)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"💰 Total Earnings: {total_earnings} AED")

    print("\n📦 Current Stock Levels:")
    for category, category_items in items.items():
        print(f"\n🔹 {category}")
        for item in category_items:
            low = "⚠️ Low!" if item['stock'] < 5 else ""
            print(f"  [{item['code']:02}] {item['name']:<16} - Stock: {item['stock']} {low}")

    print("\n📊 Analytics:")
    top_users = sorted(user_loyalty.items(), key=lambda x: x[1], reverse=True)[:3]
    print("🏅 Top Buyers:")
    for name, points in top_users:
        print(f"   {name}: {points} pts")

    print("🔥 Most Sold Items:")
    top_items = sorted(item_sales.items(), key=lambda x: x[1], reverse=True)[:5]
    for name, count in top_items:
        print(f"   {name}: {count} sold")

    while True:
        print("\n🔧 Options: [1] Restock All [2] Restock Specific [3] Reset Earnings [4] Exit Admin")
        option = input("➡️ Enter option number: ").strip()

        if option == '1':
            for category_items in items.values():
                for item in category_items:
                    item['stock'] = 100
            print("✅ All items restocked to 100.")
        elif option == '2':
            try:
                code = int(input("🔢 Enter item code to restock: "))
                item = find_item_by_code(code)
                if item:
                    new_stock = int(input(f"➕ Enter new stock for {item['name']}: "))
                    item['stock'] = new_stock
                    print(f"✅ {item['name']} stock updated to {new_stock}.")
                else:
                    print("❌ Invalid item code.")
            except ValueError:
                print("❗ Invalid input.")
        elif option == '3':
            confirm = input("⚠️ Are you sure you want to reset earnings? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                total_earnings = 0
                print("✅ Total earnings reset.")
        elif option == '4':
            break
        else:
            print("❗ Invalid option.")

def run_user_flow():
    global total_earnings
    username = input("👤 Enter your name for loyalty tracking: ").strip()
    if username not in user_loyalty:
        user_loyalty[username] = 0

    total_spent = 0
    purchased_items = []

    while True:
        display_items()
        try:
            code = int(input("📷 Scan barcode / enter item code (0 to exit): "))
        except ValueError:
            print("❗ Invalid input. Enter a number.")
            continue

        if code == 0:
            break

        item = find_item_by_code(code)
        if item:
            if item['stock'] > 0:
                print(f"\n🛒 You selected: {item['name']} - {item['price']} AED")
                handle_payment(item)
                total_spent += item['price']
                total_earnings += item['price']
                user_loyalty[username] += item['price']
                purchased_items.append(item['name'])

                extra_spent, extra_item = handle_suggestion(code)
                if extra_item:
                    total_spent += extra_spent
                    total_earnings += extra_spent
                    user_loyalty[username] += extra_spent
                    purchased_items.append(extra_item)
            else:
                print(f"❌ Sorry, {item['name']} is out of stock.")
        else:
            print("❌ Invalid item code.")

        again = input("\n🔁 Buy another item? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            break

    print("\n📋 Purchase Summary")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if purchased_items:
        for idx, name in enumerate(purchased_items, 1):
            print(f"  {idx}. {name}")
        print(f"🧾 Total Spent: {total_spent} AED")
        print(f"🎯 {username}'s Total Loyalty Points: {user_loyalty[username]} pts")
        generate_qr_receipt(purchased_items, total_spent)
    else:
        print("  No items purchased.")
    print("🙏 Thank you for shopping at Petra's Smart Vending Machine!\n")
    save_loyalty_data()

def main():
    while True:
        print("\n👋 Welcome to Petra's Smart Vending Machine 🤖")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        role = input("👤 Are you a 'user' or 'admin'? (or type 'exit' to quit): ").strip().lower()

        if role == 'exit':
            save_loyalty_data()
            print("👋 Exiting system. Have a great day!")
            break
        elif role == 'admin':
            password = input("🔑 Enter admin password: ").strip()
            
            # Admin password is hardcoded here:
            if password == "smart vending":
                admin_dashboard()
            else:
                print("❌ Authentication failed. Try again.\n")
        elif role == 'user':
            run_user_flow()
        else:
            print("❗ Invalid role. Please enter 'user' or 'admin'.")

# Start the vending machine system
main()
