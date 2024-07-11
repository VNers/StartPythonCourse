import random
import pyjokes
from art import text2art
import emoji
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style
from tqdm import tqdm
import time
import json
from data import films, stories, music, games

init(autoreset=True)
STATS_FILE = "game_stats.json"


def recommend_films():
    """Function to recommend film"""
    return random.choice(films)


def recommend_music():
    """Function to recommend music"""
    return random.choice(music)


def recommend_games():
    """Function to recommend game"""
    return random.choice(games)


def tell_joke():
    """Function to tell joke"""
    return pyjokes.get_joke()


def tell_story():
    """Function to tell story"""
    return random.choice(stories)


def load_stats():
    """Load game statistics from file"""
    try:
        with open(STATS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"wins": 0, "losses": 0, "draws": 0}


def save_stats(stats):
    """Save game statistics to file"""
    with open(STATS_FILE, "w") as file:
        json.dump(stats, file)


def play_game():
    """Function to play game"""
    stats = load_stats()
    choices = ["Stone", "Scissors", "Paper"]

    while True:
        user_choice = input(Style.BRIGHT + Fore.BLACK + "Make a choice (Stone, Scissors, Paper): ")
        computer_choice = random.choice(choices)
        print(Fore.LIGHTBLACK_EX + f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            stats["draws"] += 1
            print(Fore.LIGHTWHITE_EX + "Draw!")
        elif (user_choice == "Stone" and computer_choice == "Scissors") or \
                (user_choice == "Scissors" and computer_choice == "Paper") or \
                (user_choice == "Paper" and computer_choice == "Stone"):
            stats["wins"] += 1
            print(Fore.LIGHTWHITE_EX + "Congrats! You won!\U0001F973")
        else:
            stats["losses"] += 1
            print(Fore.LIGHTWHITE_EX + "Sorry! You lose!\U0001F614")

        save_stats(stats)

        play_again = input(Fore.LIGHTWHITE_EX + "Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break


def show_recommendations():
    """Function to show all recommendations in a table"""
    table = PrettyTable()
    table.field_names = [Fore.LIGHTWHITE_EX + "Type", "Recommendation"]
    table.add_row([Fore.LIGHTWHITE_EX + "Film", recommend_films()])
    table.add_row([Fore.LIGHTWHITE_EX + "Music", recommend_music()])
    table.add_row([Fore.LIGHTWHITE_EX + "Game", recommend_games()])
    print(table)


def show_stats():
    """Function to show game statistics"""
    stats = load_stats()
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\nGame Statistics:")
    print(Fore.LIGHTBLACK_EX + f"Wins: {stats['wins']}")
    print(Fore.LIGHTBLACK_EX + f"Losses: {stats['losses']}")
    print(Fore.LIGHTBLACK_EX + f"Draws: {stats['draws']}")


def main():
    """Main code. Interface. Work with user."""
    # tprint("Entertainment Bot", font="small")
    print(text2art("EntBot", font="medium"))
    print(emoji.emojize(Style.BRIGHT + Fore.LIGHTWHITE_EX + "Hi! This is 'Entertainment bot'! \U0001F600"))
    while True:
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\nMenu:")
        print(Fore.LIGHTBLACK_EX + "1. Movie recommendations.")
        print(Fore.LIGHTBLACK_EX + "2. Music recommendations.")
        print(Fore.LIGHTBLACK_EX + "3. Games recommendations.")
        print(Fore.LIGHTBLACK_EX + "4. Show all recommendations.")
        print(Fore.LIGHTBLACK_EX + "5. Random joke.")
        print(Fore.LIGHTBLACK_EX + "6. Short story.")
        print(Fore.LIGHTBLACK_EX + "7. Play game 'Stone, Scissors, Paper'.")
        print(Fore.LIGHTBLACK_EX + "8. Show game statistics.")
        print(Fore.LIGHTBLACK_EX + "9. Exit.")

        choice = input(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + "Choose the option: ")

        if choice == "1":
            print(Style.BRIGHT + Fore.WHITE + "Recommended movie: ", recommend_films())
        elif choice == "2":
            print(Style.BRIGHT + Fore.WHITE + "Recommended music: ", recommend_music())
        elif choice == "3":
            print(Style.BRIGHT + Fore.WHITE + "Recommended game: ", recommend_games())
        elif choice == "4":
            show_recommendations()
        elif choice == "5":
            print(Style.BRIGHT + Fore.WHITE + "Joke for you: ", tell_joke())
        elif choice == "6":
            print(Style.BRIGHT + Fore.WHITE + "Short story for you: ", tell_story())
        elif choice == "7":
            print(play_game())
        elif choice == "8":
            show_stats()
        elif choice == "9":
            print(emoji.emojize(Fore.LIGHTWHITE_EX + "Goodbye! \U0001F44B"))
            # Імітація тривалого процесу, 100 циклів
            for _ in tqdm(range(100), desc="Exiting", leave=False):
                time.sleep(0.1)
        else:
            print(Fore.RED + "Wrong choice. Try again!")


if __name__ == "__main__":
    main()
