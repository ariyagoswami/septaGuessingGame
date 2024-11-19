import random

septa_lines = [
    {"line": "Airport Line", "rating": 5},
    {"line": "Chestnut Hill East Line", "rating": 3},
    {"line": "Chestnut Hill West Line", "rating": 2},
    {"line": "Cynwyd Line", "rating": 4},
    {"line": "Fox Chase Line", "rating": 1},
    {"line": "Lansdale/Doylestown Line", "rating": 3},
    {"line": "Media/Elwyn Line", "rating": 2},
    {"line": "Manayunk/Norristown Line", "rating": 3},
    {"line": "Paoli/Thorndale Line", "rating": 2},
    {"line": "Trenton Line", "rating": 5},
    {"line": "Warminster Line", "rating": 4},
    {"line": "West Trenton Line", "rating": 3},
    {"line": "Wilmington/Newark Line", "rating": 1}
]

# Game Intro
print("SEPTA Train Rating Guessing Game")
print("You currently have 5 lives.")

def rando_train(exclude=[]):

    candidates = [train for train in septa_lines if train not in exclude]
    return random.choice(candidates) if candidates else None

def print_train(train):

    print(f"Train Line: {train['line']}")

def main():
    lives = 5
    used_septa_lines = []

    while lives > 0:
        # Select a random train line that hasn't been used yet
        train = rando_train(exclude=used_septa_lines)
        if not train:
            print("No more trains to guess!")
            break


        print_train(train)

        correct_rating = train['rating']

        while True:
            try:
                guess = int(input("How many stars in rating does this line have? (1-5): "))
                if 1 <= guess <= 5:
                    break  # Valid guess (between 1 and 5)
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        # Check if the user's guess is correct
        if guess == correct_rating:
            print("Correct!")
        else:
            print(f"Incorrect! The correct rating was {correct_rating}.")
            lives -= 1
            print(f"You have {lives} lives remaining.\n")
        used_septa_lines.append(train)


    print("Game Over!")

    if lives == 0:  # play again function
        print("Game over, you lose.")
        play_again = input("Would you like to play again? (yes/no): ").lower()  # Added space after input prompt
        if play_again == "yes":
            main()  # runs main function again
        else:
            print("Thank you for playing!")  # End game and thank the user
            # break

if __name__ == "__main__":
    main()
