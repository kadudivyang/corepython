def get_discounted_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price


# Test the function
price = 500
discount = 10

final_price = get_discounted_price(price, discount)
print("Final price:", final_price)