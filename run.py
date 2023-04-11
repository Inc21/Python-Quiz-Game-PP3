import random
from string import ascii_lowercase
from os import system, name
import gspread
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


USER_NAME = ""
while True:
    try:
        USER_NAME = input("\nPlease enter your name: ")
    except ValueError:
        print("Name must be 2 - 8 characters long.")
    if len(USER_NAME) >= 2 and len(USER_NAME) <= 8 and USER_NAME.count("  ") <= 0:
        break
    else:
        print("Name must be 2 - 8 characters long.")


def clear():
      # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def welcome_page():
    """
    Loaded up first when terminal opened with various options. 
    """
    print(f"\n Welcome to Python Quiz Game {USER_NAME}! \n")
    print("Please select one of the fallowing options (type 1, 2, 3 or 4):")
    print("1) Play the Quiz.")
    print("2) Game Instructions.")
    print("3) High Scores.")
    print("4) Exit Game.\n")

    while True:
        try:
            user_option = int(input(f"Select your next move {USER_NAME}: "))
        except ValueError:
            print("Not a valid option, please enter 1, 2, 3 or 4!")
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
    print("Game instructions\n")
    try:
        input("Press Enter to go back to main menu...")
        clear()
        welcome_page()
    except SyntaxError:
        pass


def high_scores():
    """
    Gets to top 15 high scores from google sheets and displays them on the screen.
    Also has option to return to main menu by pressing enter key.
    """
    print("High Scores for Google Sheets\n")
    try:
        input("Press Enter to go back to main menu...")
        welcome_page()
    except SyntaxError:
        pass


def game_over():
    """
    This function is loaded when user answers a question wrong and giving them option to play again.
    """
    game_over_user = input("Would you like to play again? Type Y for yes or Q to quit: ").lower()
    if game_over_user == "q":
        clear()
        exit()
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
    questions = random.sample(list(QUESTIONS.items()), len(QUESTIONS))
    points = 0
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f" {label}) {alternative}")

        while (answer_label := input("\nYour selection? ").lower()) not in labeled_alternatives:
            if answer_label == "q":
                exit()
            print(f"Not a valid option, please enter {','.join(labeled_alternatives)} or q to quit")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            clear()
            print("\nCORRECT!\n")
            points += 10
            num_correct += 1
            print(f"Your have {points} points.")
        else:
            print( f"The answer is {correct_answer!r}, not {answer!r}\n")
            print("Game Over")
            print(f"\nYou scored {points} points by answering {num_correct} questions correctly.\n")
            game_over()


def main():
    """
    Run all program functions.
    """
    welcome_page()
    # run_game()


main()
