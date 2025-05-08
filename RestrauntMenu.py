menu = {
    'Espresso': 400,
    'Latte': 500,  # Fixed extra space in 'Latte '
    'Macchiato': 700,
    'Cappuccino': 800,
}

# Greet
print("Welcome to COFFEE SHOP\n")
print("Espresso: Rs400\nLatte: Rs500\nMacchiato: Rs700\nCappuccino: Rs800")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")  # Fixed string formatting
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another order? (yes/no): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")  # Fixed string formatting
    else:
        print(f"Ordered item {item_2} is not available.")

print(f"The total amount of items is Rs{order_total}") 