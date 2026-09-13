name = input("what is your name? ")
name_game = input("what is the game name? ")

rate = input("pls enter a rate: ")

while True:
    if int(rate) < 0 or int(rate) > 5:
        print("plaese enter a number from 1 to 5")
    break

review = input("write short review: ")

with open("game_reviews.txt", "a") as file:
    file.write(f"{name} - {name_game} - {rate}/5 - {review}\n")