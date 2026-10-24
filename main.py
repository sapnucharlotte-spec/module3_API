import requests
import random

pokemon_list = ["pikachu", "snorlax", "bulbasaur", "mew", "sylveon"]

pokemon_name = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/{pokemon_name}"
response = requests.get(url)

attempt = 3

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]

    print("POKEMON GUESS GAME!")
    print("Guess the name of the Pokemon")
    print("You have 3 attempts")
    print("Height: {height}")
    print("Weight: {weight}")
    input("You Answer:")

    for i in range(1, 4):
        guess = input (f"Attempt {attempt}/3 - Guess the Pokemon:")

        if guess == name:
            print("Your Guess is Correct!")
            break
        else:
            print("Wrong guess! Nice try.")

    else: 
        print("Game Over! Thanks for playing!")

elif response.status_code == 404:
    print("Pokemon not found, Please check the Pokemon name.")
else:
    print("Something went wrong.", response.status_code)