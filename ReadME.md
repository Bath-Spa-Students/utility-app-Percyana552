Petra's Smart Vending Machine

Hi! I'm Petras, and this is a Python-based simulation of a smart vending machine that runs in the terminal. I built this to mimic the experience of using a real, modern vending machine—complete with a loyalty system, multiple payment methods, admin tools, and even smart product suggestions.

What This Project Does

The vending machine runs in two modes:

User Mode
As a user, you can:

Browse and buy items like snacks, drinks, sweets, and coffee
Pay using cash, card, biometric sensor, Apple Pay, or Google Pay
Get suggestions for paired items (like Pepsi and Cookies)
Earn loyalty points based on how much you spend
Receive a text-style receipt at the end of your purchase
Admin Mode
As the admin, you can:

See total earnings
View items that are running low on stock
Restock specific items or everything at once
See the top buyers and most sold items
Reset sales totals when needed
The admin section is password-protected with: smart vending.

Item Categories

Here are the types of products included in the machine:

Drinks – Pepsi, Coca Cola, Lacnor, etc.
Snacks – Pringles, Chips, Cashews
Sweets – Cupcakes, Cake, Muffins
Coffee – Espresso, Latte, Americano
Each product has:

A unique item code
A price (in AED)
A stock quantity
An optional suggested pairing (for cross-selling)
Payment Methods

Users can choose from:

Cash (with change calculated)
Credit or Debit Card
Biometric scan (hand or eye)
Apple Pay
Google Pay
Loyalty System

I added a simple loyalty system where:

You earn 1 point per 1 AED spent
Points are saved using a file called loyalty_data.json
Your name is used to track your points across sessions
At the end of a purchase, your updated total points are shown
Admin Dashboard Features

Once logged in as admin, you can:

See how much money the machine has made
Check which items are running low
Restock items
View the most popular items and top buyers
Reset all totals to start fresh
Main Files and Functions

Here’s a quick look at the main parts of the code:

main() — Starts the program
run_user_flow() — Handles all user interactions
admin_dashboard() — All admin controls and views
handle_payment() — Processes the payment options
handle_suggestion() — Offers product pairings
generate_qr_receipt() — Creates a text-style receipt
display_items() — Shows what's available
save_loyalty_data() — Saves points and names in JSON
How to Use It

Run the Python file in your terminal.
Choose whether you're a user or admin.
As a user:
Type in your name to track points
Pick an item by its code
Choose how you want to pay
Accept or skip the smart pairing suggestion
Finish the payment and get your receipt
As an admin:
Enter the admin password
Review sales, top items, or restock as needed
Reset earnings if you want a fresh start
Saving Data

Loyalty points are stored between sessions using loyalty_data.json
Stock levels and earnings reset when the program restarts (unless extended with saving logic)
Smart Suggestions

Some items come with a suggested pairing from a different category. If the user accepts:

The item is added to the purchase
Stock levels update
Points are added
The receipt is updated
Validation and Security

Admin mode is password-protected
Inputs are validated (e.g., item codes, payment choices)
The system checks for out-of-stock items and handles mistakes nicely
Requirements

Python 3.x
No external libraries just run the script in any terminal
Sample Run
<img width="1411" alt="Screenshot 2025-07-02 at 3 51 39 PM" src="https://github.com/user-attachments/assets/4d4b3b44-7972-4073-a355-23cdf27095de" />
About Me

I'm Petras, and I built this project to combine fun with functionality. It’s a hands-on simulation to explore concepts like automation, smart retail, and user engagement in Python. I hope you find it useful or inspiring!
