import random
import requests

pokemon_list = ["pikachu", "snorlax", "bulbasaur", "mew", "sylveon"]

pokemon_name = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    name = data["name"].capitalize()
    height = data["height"]
    weight = data["weight"]
    skill = data["abilities"][0]["ability"]["name"]

    print("WHO'S THAT POKEMON?")
    print("Guess the name of the Pokemon")
    print("You have 3 attempts\n")
    print("Height: {height}")
    print("Weight: {weight}")
     print(f"Skill: {skill}\n")

    while True:
        for attempt in range(1, 4):
            guess = input(f"Attempt {attempt}/3 - Guess the Pokemon: ").strip().lower()

            if guess == name.lower():
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