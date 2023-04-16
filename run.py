import random
from string import ascii_lowercase
import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
import os
from time import sleep
from tabulate import tabulate
from google.oauth2.service_account import Credentials
import pyfiglet
import gspread
from colored import fg, attr

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Colour variables
GR = fg("dark_olive_green_2")
RD = fg("red")
GD = fg("gold_3a")
YL = fg("yellow")
BL = fg("blue")
R = attr("reset")

# Constant variables.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_leaderboard')
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())
ASCII_BANNER = GR + pyfiglet.figlet_format("Python Quiz Game.", font="rectangles") + R

# Global variables that will be defined in functions.
USER_NAME = ""
POINTS = 0


def welcome_page():
    """
    Loaded up first when terminal opened, greets user and asks for their name.
    """
    global USER_NAME
    print(ASCII_BANNER)
    while True:
        try:
            USER_NAME = input(YL + "Please enter your name: " + R)
        except ValueError:
            print(RD + """\nInvalid entry!
Name must be 2 - 10 characters long and can't contain 2 or more spaces.\n""" +
R)
        if (len(USER_NAME) >= 2 and len(USER_NAME) <= 10 and
                USER_NAME.count("  ") <= 0):
            break
        else:
            print(RD + """\nInvalid entry!
Name must be 2 - 10 characters long and can't contain 2 or more spaces.\n""" +
R)


def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
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
    ascii_main_menu = GR + pyfiglet.figlet_format("Main Menu.", font="rectangles") + R
    print(ascii_main_menu)
    print(f"Welcome to the {GR}Python quiz game{R} {USER_NAME}")
    print("Please select one of the fallowing options (type 1, 2, 3 or 4):\n ")
    print("1) Play the Quiz.")
    print("2) Game Instructions.")
    print("3) High Scores.")
    print("4) Exit Game.\n")

    while True:
        try:
            user_option = int(input(f"{YL}Select your next move {USER_NAME}: {R}"))
        except ValueError:
            print(f"\n{RD}Not a valid entry! Please enter 1, 2, 3 or 4!{R}\n")
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
        else:
            print(f"\n{RD}Not a valid entry! Please enter 1, 2, 3 or 4!{R}")


def game_instructions():
    """
    Displays game instructions. Includes option to return to main
    menu by pressing enter key.
    """
    ascii_instructions = GR + pyfiglet.figlet_format("Instructions.", font="rectangles") + R
    print(ascii_instructions)
    print("To play the game, all you have to do is answer all\
 25 questions correctly.")
    print("Simple really isn't it?\n")
    print("To select your answer, enter corresponding letter and hit enter.")
    print("Every correct answer is worth 10 points.\n")
    print("Get question wrong and your game is over.")
    print("Your points are recorded and uploaded to the database.\n")
    print("Hopefully you did well enough to be in top 10 and see your name on\
 the leaderboard.\n")
    print("To end the game during play, you can enter letter Q to return to\
 main menu")
    print("but points you worked so hard to get are lost forever.\n")
    try:
        input(f" {YL}-> Press Enter to go back to main menu...{R}")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def high_scores():
    """
    Gets to top 10 high scores from google sheets and displays them on
    the screen. Using tabulate prints top 10 results. Sorts results
    using sort(). Also has option to return to main menu by pressing enter key.
    """
    ascii_hi_scores = GR + pyfiglet.figlet_format("High Scores.", font="rectangles") + R
    print(ascii_hi_scores)
    SHEET.sheet1.sort((2, 'des'))
    page = SHEET.sheet1.get_all_values()
    print(tabulate(page[0:10], headers=["NAME", "POINTS"]))
    try:
        input("\n-> Press Enter to go back to main menu...")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def game_over():
    """
    This function is loaded when user answers a question wrong and giving them
    option to play again. Uploads final score to Google sheets.
    """
    while True:
        try:
            game_over_user = input("""Would you like to play again?
Type Y for yes or Q to go back to main menu: """).lower()
        except ValueError:
            print("\nNot a valid option, please enter Y or Q\n")
        if game_over_user == "q":
            clear()
            main_menu_page()
        elif game_over_user == "y":
            clear()
            run_game()
        else:
            clear()
            print("\nNot a valid option, please enter Y or Q\n")


def run_game():
    """
    Run the main Quiz Game. Get question from question.toml.
    Checks user input (correct answer index 0).
    Displays next question if answer correct otherwise, game over.
    """
    global POINTS
    ascii_correct = GR + pyfiglet.figlet_format("Correct!", font="rectangles") + R
    ascii_game_over = RD + pyfiglet.figlet_format("Game Over!", font="rectangles") + R
    ascii_winner = GD + pyfiglet.figlet_format("Winner Winner!", font="rectangles") + R
    questions = random.sample(list(QUESTIONS.items()), len(QUESTIONS))
    POINTS = 0
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(ASCII_BANNER)
        print(f"\nQuestion {num}:")
        print(f"{question}")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f" {label}) {alternative}")
        if num_correct == 25:
            clear()
            print(ascii_winner)
            print(f"Well done {USER_NAME} you great Python master!")
            print(f"You scored {POINTS} points by answering all {num_correct}\
 questions correctly.\n")
            print("Another 250 points will be added to your tally")
            print("for getting them all correctly.\n")
            POINTS += 250
            update_leaderboard()
            game_over()
            return

        while ((answer_label := input("\nYour selection? ").lower()) not in
               labeled_alternatives):
            if answer_label == "q":
                clear()
                main_menu_page()
            print(f"""\nNot a valid option!
Please enter {','.join(labeled_alternatives)} or Q to quit to main menu""")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            clear()
            print(ascii_correct)
            POINTS += 10
            num_correct += 1
            print(f"Your have {POINTS} points.")
            sleep(2)
            clear()
        elif answer != correct_answer and num_correct == 0:
            clear()
            print(ascii_game_over)
            print(f"\nOops {USER_NAME}!")
            print(f"The correct answer is {correct_answer!r}, not {answer!r}")
            print("You scored no points this round.\n")
            game_over()
        else:
            clear()
            print(ascii_game_over)
            print(f"""The correct answer is {correct_answer!r},
not {answer!r}\n""")
            print(f"\nNicely done {USER_NAME}!")
            print(f"""You scored {POINTS} points by answering {num_correct}
questions correctly.\n""")
            update_leaderboard()
            game_over()


def update_leaderboard():
    """
    Update the worksheet with the user name and their final points.
    """
    data = USER_NAME, POINTS
    print("Updating leaderboard...\n")
    leaderboard_sheet = SHEET.worksheet("main")
    leaderboard_sheet.append_row(data)
    print("Leaderboard updated successfully.\n")


def main():
    """
    Run all program functions.
    """
    welcome_page()
    clear()
    main_menu_page()


main()
