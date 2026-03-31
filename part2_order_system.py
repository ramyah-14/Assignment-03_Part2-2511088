menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# Task 1 — Explore the Menu
categories = ["Starters", "Mains", "Desserts"]

#loop through the menu
for category in categories:
    print(f"\n===== {category} =====")
    for item_name, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"  {item_name}  ₹{details['price']:.2f}  [{status}]")
#full menu grouped by category
total_items     = len(menu)
available_items = sum(1 for d in menu.values() if d["available"])
most_expensive  = max(menu.items(), key=lambda x: x[1]["price"])

#Total , Available , Expensive and Under 100 Items
print(f"\nTotal items    : {total_items}")
print(f"Available items: {available_items}")
print(f"Most expensive : {most_expensive[0]}  ₹{most_expensive[1]['price']:.2f}")


print("\nItems under ₹150:")
for name, d in menu.items():
    if d["price"] < 150:
        print(f"  {name}  ₹{d['price']:.2f}")



# Task 2 — Cart Operations
cart = []

#add to cart
def add_to_cart(item_name, qty):
    if item_name not in menu:
        print(f"'{item_name}' does not exist in the menu")
        return
    #unavailable item
    if not menu[item_name]["available"]:
        print(f"'{item_name}' is currently unavailable")
        return
    #increase quantity for already existing item
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += qty
            print(f"Updated quantity: {item_name} is now x{item['quantity']}")
            return
    cart.append({"item": item_name, "quantity": qty, "price": menu[item_name]["price"]})
    print(f"Added to cart: {item_name} x{qty}")

#remove from cart by name
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed from cart: {item_name}")
            return
    print(f"'{item_name}' was not in the cart")


add_to_cart("Paneer Tikka", 2)
print("Cart:", cart)


add_to_cart("Gulab Jamun", 1)
print("Cart:", cart)


add_to_cart("Paneer Tikka", 1)   # should update quantity to 3
print("Cart:", cart)


add_to_cart("Mystery Burger", 1)  # does not exist
add_to_cart("Chicken Wings", 1)   # unavailable


remove_from_cart("Gulab Jamun")
print("Cart:", cart)

#printing final order summary
print("\n========== Order Summary ==========")
subtotal = 0
for item in cart:
    line_total = item["quantity"] * item["price"]
    subtotal += line_total
    print(f"  {item['item']} x{item['quantity']}   ₹{line_total:.2f}")
gst   = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)
print("-" * 36)
print(f"Subtotal     : ₹{subtotal:.2f}")
print(f"GST (5%)     : ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")
print("====================================")





# Task 3 — Inventory
import copy
inventory_backup = copy.deepcopy(inventory)


# Prove the deep copy works
inventory["Dal Tadka"]["stock"] = 999
print("inventory Dal Tadka stock:",        inventory["Dal Tadka"]["stock"])
print("inventory_backup Dal Tadka stock:", inventory_backup["Dal Tadka"]["stock"])
inventory["Dal Tadka"]["stock"] = 20   # restore original

#deduct items in inventory based on the cart from task 2
for cart_item in cart:
    name = cart_item["item"]
    qty  = cart_item["quantity"]
    available_stock = inventory[name]["stock"]
    if available_stock < qty:
        print(f"Warning: only {available_stock} of {name} available, deducting that amount")
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= qty

#print("inventory  :",        inventory["Paneer Tikka"]["stock"])        

#printing reorder details
print("\nReorder Alerts:")
for name, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

#printing inventory and inventory backup
print("\n\n")
print("Inventory")
print("-" * 60)
print(f"{'Item':<20} {'Stock':>6} {'Reorder Level':>15} ")
print("-" * 60)

#Inventory
for name, data in inventory.items():
        #print(f"Item {name} - Stock Left {data['stock']}, Reorder Level {data['reorder_level']}")
        print(f"{name:<20} {data['stock']:>3} {data['reorder_level']:>15}")
print("\n\n")
print("Inventory Backup")
print("-" * 60)
print(f"{'Item':<20} {'Stock':>6} {'Reorder Level':>15} ")
print("-" * 60)

#Inventory Backup
for name, data in inventory_backup.items():
        #print(f"Item {name} - Stock Left {data['stock']}, Reorder Level {data['reorder_level']}")
        print(f"{name:<20} {data['stock']:>3} {data['reorder_level']:>15}")        


# Task 4 — Sales Log
print("\nRevenue per day:")
for date, orders in sales_log.items():
    day_total = sum(order["total"] for order in orders)
    print(f"  {date}: ₹{day_total:.2f}")

#Best day
best_day = max(sales_log.keys(), key=lambda d: sum(o["total"] for o in sales_log[d]))
print(f"\nBest selling day: {best_day}")

#Most Ordered Item
item_count = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1
most_ordered = max(item_count, key=item_count.get)
print(f"Most ordered item: {most_ordered} (in {item_count[most_ordered]} orders)")

#Add new day and Reprint
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]


print("\nUpdated revenue per day:")
for date, orders in sales_log.items():
    day_total = sum(order["total"] for order in orders)
    print(f"  {date}: ₹{day_total:.2f}")
best_day = max(sales_log.keys(), key=lambda d: sum(o["total"] for o in sales_log[d]))
print(f"New best selling day: {best_day}")

#Enumerate All orders
print("\nAll orders:")
counter = 1
for date in sorted(sales_log.keys()):
    for order in sales_log[date]:
        items_str = ", ".join(order["items"])
        print(f"{counter}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")
        counter += 1



