import random
import requests

pokemon_list = ["pikachu", "snorlax", "bulbasaur", "mew", "sylveon"]

while True:
    pokemon_name = random.choice(pokemon_list)

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
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
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Skill: {skill}\n")


        for attempt in range(1, 4):
            guess = input(f"Attempt {attempt}/3 - Guess the Pokemon: ").strip().lower()

            if guess == name.lower():
                print(f"Correct! The Pokemon is {name}!\n")
                break
            else:
                print("Wrong guess! Nice try :3\n")
        else: 
            print(f"Game over! The correct Pokemon was {name}.")

        while True:
            choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

            if choice == "yes":
                print("\nStarting a new game!\n")
                break 
            elif choice == "no":
                print("Thanks for playing! Goodbye!")
                exit()
            else:
                print("Invalid choice.")

    elif response.status_code == 404:
        print("Pokemon not found, Please check the Pokemon name.")
        break
    else:
        print("Something went wrong.", response.status_code)
        break