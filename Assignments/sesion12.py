def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price
# Test the function
price = 500
discount_percent = 10
print("Final price:", get_discounted_price(price, discount_percent))

#
def format_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)
# Test the function
print(format_follower_count(1500))
print(format_follower_count(1200000))
print(format_follower_count(850))


song_durations = [3, 4, 5, 2.5]
# Convert minutes to seconds using lambda and map()
durations_in_seconds = list(map(lambda minutes: minutes * 60, song_durations))
print(durations_in_seconds)

products = ["Mobile", "Mouse", "Laptop", "Monitor", "Keyboard"]
# Filter products starting with 'M'
m_products = list(filter(lambda product: product.startswith("M"), products))
print(m_products)


from functools import reduce
item_prices = [120, 80, 150, 60]
total_bill = reduce(lambda x, y: x + y, item_prices)
print("Total bill:", total_bill)
