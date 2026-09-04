my_playlist = {
    "Shape of You": 4.24,
    "Blinding Lights": 3.20,
    "Perfect": 4.23
}
print(my_playlist)


my_playlist = {
    "Shape of You": 4.24,
    "Blinding Lights": 3.20,
    "Perfect": 4.23
}
# Add a new song
my_playlist["Believer"] = 3.24
# Update the duration of an existing song
my_playlist["Perfect"] = 4.40
print(my_playlist)


def display_friends(friends):
    for username, followers in friends.items():
        if followers >= 1000:
            follower_count = f"{followers / 1000:.1f}K"
        else:
            follower_count = str(followers)

        print(f"{username}: {follower_count} followers")
# Example
friends = {
    "rahul123": 2300,
    "priya_music": 1500,
    "amit_07": 850
}
display_friends(friends)


food_order = {
    "Pizza": 2,
    "Burger": 1,
    "Fries": 3
}
# a) Print all food items
print("Food items:", food_order.keys())
# b) Print all quantities
print("Quantities:", food_order.values())
# c) Print each item with its quantity
print("Items with quantities:")
for item, quantity in food_order.items():
    print(item, ":", quantity)

def update_cart(cart, item, qty):
    cart[item] = qty
    return cart
# Example cart
cart = {
    "Laptop": 1,
    "Mouse": 2
}
# Add a new item
cart = update_cart(cart, "Keyboard", 1)
print(cart)
# Update an existing item
cart = update_cart(cart, "Mouse", 3)
print(cart)

