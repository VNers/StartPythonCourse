import random
import pyjokes
from art import tprint, text2art
import emoji
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style
from tqdm import tqdm



init(autoreset=True)

films = [Fore.BLACK + "Avatar", Fore.BLACK + "Great Gatsby", Fore.BLACK + "Oppenheimer", Fore.BLACK + "Titanic",
         Fore.BLACK + "Brain Games"]
music = [Fore.BLACK + "Dance", Fore.BLACK + "Flowers", Fore.BLACK + "Cold Heart", Fore.BLACK + "We will rock you",
         Fore.BLACK + "Halo"]
games = [Fore.BLACK + "Battlefield", Fore.BLACK + "Dota2", Fore.BLACK + "Lineage2", Fore.BLACK + "CS.GO",
         Fore.BLACK + "Last of us"]
jokes = [Fore.BLACK + "Why are snails slow? Because they’re carrying a house on their back.",
         Fore.BLACK + "What’s the smartest insect? A spelling bee!",
         Fore.BLACK + "How does the ocean say hi? It waves!",
         Fore.BLACK + "What do birds give out on Halloween? Tweets.",
         Fore.BLACK + "What is a room with no walls? A mushroom."]
stories = [Fore.BLACK + "The Rainbow Fish: This short story tells that\nthe rainbow fish wants to know who he is by "
                        "pointing to the \nindividual identity and the morality of life.",
           Fore.BLACK + "The Very Hungry Caterpillar:This story about a caterpillar journey \nas the hungry caterpillar"
                        "transforms into a beautiful butterfly.",
           Fore.BLACK + "The Little Red Hen:This story tells the importance of being hardworking,\ncooperative and "
                        "helping others in this classical children tale.",
           Fore.BLACK + "The Ugly Duckling: This story is a popular children tale about acceptance \nof someone’s "
                        "appearance and finding one’s true identity.",
           Fore.BLACK + "Cinderella: The classic fairytale of Cinderella about kindness, love magic, \nand a happily "
                        "ever after."]


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
    return random.choice(jokes)
    #return pyjokes.get_joke()


def tell_story():
    """Function to tell story"""
    return random.choice(stories)


def play_game():
    """Function to play game"""
    choices = ["Stone", "Scissors", "Paper"]
    user_choice = input(Style.BRIGHT + Fore.BLACK + "Make a choice (Stone, Scissors, Paper): ")
    computer_choice = random.choice(choices)
    print(Fore.LIGHTBLACK_EX + f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        return Fore.LIGHTWHITE_EX + "Draw! "
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Stone"):
        return Fore.LIGHTWHITE_EX + "Congrats! You won!\U0001F973"
    else:
        return Fore.LIGHTWHITE_EX + "Sorry! You lose!\U0001F614"


def show_recommendations():
    """Function to show all recommendations in a table"""
    table = PrettyTable()
    table.field_names = [Fore.LIGHTWHITE_EX + "Type", "Recommendation"]
    table.add_row([Fore.LIGHTWHITE_EX + "Film", recommend_films()])
    table.add_row([Fore.LIGHTWHITE_EX + "Music", recommend_music()])
    table.add_row([Fore.LIGHTWHITE_EX + "Game", recommend_games()])
    print(table)


def main():
    """Main code. Interface. Work with user."""
    #tprint("Entertainment Bot", font="small")
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
        print(Fore.LIGHTBLACK_EX + "8. Exit.")

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
            print(emoji.emojize(Fore.LIGHTWHITE_EX + "Goodbye! \U0001F44B"))
            for _ in tqdm(range(100), desc="Exiting", leave=False):
                pass
            break
        else:
            print(Fore.RED + "Wrong choice. Try again!")


if __name__ == "__main__":
    main()
