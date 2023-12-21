import random
from Gamedata import data
from Gamedata import logo
from Gamedata import vs

end_game = False
score = 0


def higher(x, y):
    if x > y:
        return "A"
    else:
        return "B"


while not end_game:

    higher_val = ""
    data_a = data[random.randint(0, 50)]
    data_b = data[random.randint(0, 50)]

    if data_b == data_a:
        data_b = data_b + 1

    data_a_name = data_a["name"]
    data_a_description = data_a["description"]
    data_a_country = data_a["country"]
    data_a_val = data_a["follower_count"]

    data_b_name = data_b["name"]
    data_b_description = data_b["description"]
    data_b_country = data_b["country"]
    data_b_val = data_b["follower_count"]

    print(logo)

    print(f"Compare A: {data_a['name']}, a {data_a_description}, from {data_a_country}")

    print(vs)

    print(f"Against B: {data_b['name']}, a {data_b_description}, from {data_b_country}")
    user = input("Who has more followers? Type 'A' or 'B':").upper()

    higher_val = higher(data_a_val, data_b_val)

    if user == higher_val:
        score = score + 1
        print(f"You're right! Current score: {score}")

    else:
        end_game = True
        print(f"Sorry, that's wrong. Final score: {score}")
