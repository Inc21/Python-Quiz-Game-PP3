import random
from string import ascii_lowercase
import os
from time import sleep
import gspread
import pyfiglet
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_leaderboard')
USER_NAME = ""
ascii_banner = pyfiglet.figlet_format("Python Quiz Game.", font="rectangles")


QUESTIONS =  {
    "How is a code block indicated in Python?": [
        "Indentation", "Brackets", "Key", "None of the above"
    ],
    "What is the maximum length of a Python identifier?": [
        "No fixed length is specified", "32", "16", "128"
    ],
    "Which of the following concepts is not a part of Python?": [
        "Pointers", "Loops", "Dynamic Typing", "All the above"
    ],
    "Which of the following statements are used in Exception Handling in Python?": [
        "All of the above", "try", "except", "finally"   
    ],
}


def welcome_page():
    """ 
    Loaded up first when terminal opened, greets user and asks for their name.
    """
    global USER_NAME
    print(ascii_banner)
    while True:
        try:
            USER_NAME = input("Please enter your name: ")
        except ValueError:
            print("""\nInvalid entry!
Name must be 2 - 8 characters long and can't contain 2 or more spaces.\n""")
        if len(USER_NAME) >= 2 and len(USER_NAME) <= 8 and USER_NAME.count("  ") <= 0:
            break
        else:
            print("""\nInvalid entry!
Name must be 2 - 8 characters long and can't contain 2 or more spaces.\n""")
    return USER_NAME


def clear():
    """
    Function to clear the terminal on windows, mac and linux for a better user experience.
    """
      # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def main_menu_page():
    """
     with various options. 
    """
    ascii_main_menu = pyfiglet.figlet_format("Main Menu.", font="rectangles")
    # print(f"\n Welcome to Python Quiz Game {USER_NAME}! \n")
    print(ascii_main_menu)
    print(f"Welcome to the Python quiz game {USER_NAME}")
    print("Please select one of the fallowing options (type 1, 2, 3 or 4):\n ")
    print("1) Play the Quiz.")
    print("2) Game Instructions.")
    print("3) High Scores.")
    print("4) Exit Game.\n")

    while True:
        try:
            user_option = int(input(f"Select your next move {USER_NAME}: "))
        except ValueError:
            print("\nNot a valid entry! Please enter 1, 2, 3 or 4!\n")
        else:
            break
    if user_option == 1:
        clear()
        run_game()
    elif user_option == 2:
        clear()
        game_instructions()
    elif user_option == 3:
        clear()
        high_scores()
    elif user_option == 4:
        clear()
        exit()


def game_instructions():
    """
    Displays game instructions. Includes option to return to main
    menu by pressing enter key.
    """
    ascii_instructions = pyfiglet.figlet_format("Instructions.", font="rectangles")
    print(ascii_instructions)
    try:
        input("Press Enter to go back to main menu...")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def high_scores():
    """
    Gets to top 15 high scores from google sheets and displays them on the screen.
    Also has option to return to main menu by pressing enter key.
    """
    ascii_high_scores = pyfiglet.figlet_format("High Scores.", font="rectangles")
    print(ascii_high_scores)
    print("High Scores from Google Sheets.\n")
    try:
        input("Press Enter to go back to main menu...")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def game_over():
    """
    This function is loaded when user answers a question wrong and giving them option to play again.
    Uploads final score to Google sheets.
    """
    game_over_user = input("""Would you like to play again?
Type Y for yes or Q to go bact to main menu: """).lower()
    if game_over_user == "q":
        clear()
        main_menu_page()
    elif game_over_user == "y":
        clear()
        run_game()
    else:
        print("\nNot a valid option, please enter Y or Q\n")
        game_over()


def run_game():
    """
    Run the main Quiz
    """
    ascii_correct = pyfiglet.figlet_format("Correct!", font="rectangles")
    ascii_game_over = pyfiglet.figlet_format("Game Over!", font="rectangles")
    questions = random.sample(list(QUESTIONS.items()), len(QUESTIONS))
    points = 0
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(ascii_banner)
        print(f"\nQuestion {num}:")
        print(f"{question}")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f" {label}) {alternative}")

        while (answer_label := input("\nYour selection? ").lower()) not in labeled_alternatives:
            if answer_label == "q":
                clear()
                main_menu_page()
            print(f"""\nNot a valid option!
Please enter {','.join(labeled_alternatives)} or q to quit to main menu""")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            clear()
            print(ascii_correct)
            points += 10
            num_correct += 1
            print(f"Your have {points} points.")
            sleep(3)
        else:
            clear()
            print(ascii_game_over)
            print( f"The answer is {correct_answer!r}, not {answer!r}\n")
            print(f"""\nNicely done {USER_NAME}!
You scored {points} points by answering {num_correct} questions correctly.\n""")
            game_over()


def main():
    """
    Run all program functions.
    """
    welcome_page()
    clear()
    main_menu_page()


main()
