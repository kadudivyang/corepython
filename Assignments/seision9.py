my_fav_apps = ["Instagram", "WhatsApp", "Spotify", "Zomato", "YouTube"]
print(my_fav_apps)


my_fav_apps = ["Instagram", "WhatsApp", "Spotify", "Zomato", "YouTube"]
my_fav_apps.append("Flipkart")
print(my_fav_apps)


my_fav_apps = ["Instagram", "Spotify", "Zomato", "YouTube", "Flipkart"]
my_fav_apps.insert(1, "WhatsApp")
print(my_fav_apps)


my_fav_apps = ["Instagram", "WhatsApp", "Spotify", "Zomato", "YouTube", "Flipkart"]

# Remove an app you no longer use
my_fav_apps.remove("Zomato")
print("After remove():", my_fav_apps)

# Remove the last app
my_fav_apps.pop()
print("After pop():", my_fav_apps)


my_fav_apps = ["Instagram", "WhatsApp", "Spotify", "YouTube", "Flipkart"]
# Sort in alphabetical order
my_fav_apps.sort()
print("Alphabetical order:", my_fav_apps)
# Reverse the order
my_fav_apps.reverse()
print("Reversed order:", my_fav_apps)
