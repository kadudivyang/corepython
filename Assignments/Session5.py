food_apps = ["Zomato", "Swiggy", "Domino's", "McDonald's", "Pizza Hut"]

for app in food_apps:
    print(app)


user_bio = "Music lover | Foodie | Traveller"

count = 0

for char in user_bio:
    if char != " ":
        count += 1

print("Number of characters excluding spaces:", count)

fav_movies = ["3 Idiots", "Dangal", "KGF"]

for movie in fav_movies:
    print(movie.upper())


word = input("Enter a word: ")

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char)

