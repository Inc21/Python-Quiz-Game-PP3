import random
from string import ascii_lowercase
import pathlib
# import tomli as tomllib. Was added because of backwards compatibility.
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
RD = fg("light_red")
GD = fg("gold_3a")
YL = fg("light_yellow")
BL = fg("turquoise_2")
R = attr("reset")

# Constant variables.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_leaderboard')
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

ASCII_BANNER = GR + pyfiglet.figlet_format(
    "Python Quiz Game.", font="rectangles", justify="center"
    ) + R
ASCII_GAME_OVER = RD + pyfiglet.figlet_format(
        "Game Over!", font="rectangles", justify="center"
        ) + R

# Global variables that will be defined in functions.
USER_NAME = ""
POINTS = 0


def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system('clear')


def welcome_page():
    """
    Loaded up first when the terminal opened, greets the user and asks for
    their name.
    """
    global USER_NAME
    print(ASCII_BANNER)
    while True:
        try:
            USER_NAME = input(YL + "Please enter your name:\n" + R)
        except ValueError:
            clear()
            print(ASCII_BANNER)

            print(f"\n{USER_NAME}{RD} is invalid entry!")
            print("Name must be 2 - 10 characters")
            print(f"long and can't contain 2 or more spaces.{R}\n")
        if (len(USER_NAME) >= 2 and len(USER_NAME) <= 10 and
                USER_NAME.count("  ") <= 0):
            break
        else:
            clear()
            print(ASCII_BANNER)
            print(f"\n{USER_NAME}{RD} is invalid entry!")
            print("Name must be 2 - 10 characters")
            print(f"long and can't contain 2 or more spaces.{R}\n")


def main_menu_page():
    """
     Loads "Main menu" with 4 game options.
     Also checks for valid input.
    """
    def menu_options():
        """
        Nested function to be printed on the screen after users
        repeated non valid entries.
        """
        print(ASCII_BANNER)
        print(f"Welcome {BL + USER_NAME + R}!")
        print(
            f"Please select {YL}1, 2, 3 or 4{R} from the Main Menu below.\n "
            )
        print(f"{YL}1){R} Play the Quiz.")
        print(f"{YL}2){R} Game Instructions.")
        print(f"{YL}3){R} High Scores.")
        print(f"{YL}4){R} Exit Game.\n")

    menu_options()
    while True:
        user_option = 0
        try:
            user_option = (int(input(f"{YL}Whats's your next move\
 {BL + USER_NAME}{YL}? {R}\n")))
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
                print(ASCII_BANNER)
                print(f"{YL}\
                Thanks for playing Python Quiz Game {BL}{USER_NAME}!{R}")
                sleep(4)
                exit()
            else:
                clear()
                menu_options()
                sleep(0.2)
                print(f"{RD}Not a valid entry!{R}")
                print(f"{RD}Please enter 1, 2, 3 or 4!{R}\n")
        except ValueError:
            clear()
            menu_options()
            sleep(0.2)
            print(f"{RD}Not a valid entry!{R}")
            print(f"{RD}Please enter 1, 2, 3 or 4!{R}\n")


def game_instructions():
    """
    Displays game instructions. Includes option to return to main
    menu by pressing enter key.
    """
    ascii_instructions = GR + pyfiglet.figlet_format(
        "Instructions.", font="rectangles", justify="center"
        ) + R
    print(ascii_instructions)
    print("To play the game, all you have to do is answer all")
    print("25 questions correctly.")
    print("Simple really isn't it?\n")
    print("To select your answer, enter corresponding letter and hit enter.")
    print("Every correct answer is worth 10 points.\n")
    print("When you get all 25 correct, bonus will be added to your score.\n")
    print("Get question wrong and your game is over.")
    print("Your points are recorded and uploaded to the database.\n")
    print("Hopefully you did well enough to be in top 10 and see your")
    print("name on the leaderboard.\n")
    print("To end the game during play, you can enter letter Q to")
    print("return to main menu")
    print("but points you worked so hard to get, are lost forever.\n")
    try:
        input(f" {YL}-> Press Enter to go back to main menu...{R}\n")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def high_scores():
    """
    Gets to top 10 high scores from google sheets and displays them on
    the screen. Using tabulate prints top 10 results. Sort results
    using sort(). Also has the option to return to the main menu by pressing
    enter key.
    """
    ascii_hi_scores = GR + pyfiglet.figlet_format(
        "High Scores.", font="rectangles", justify="center"
        ) + R
    print(ascii_hi_scores)
    SHEET.sheet1.sort((2, 'des'))
    row_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    page = SHEET.sheet1.get_all_values()
    print(tabulate(page[0:10], headers=["POSITION", "NAME", "POINTS"],
                   tablefmt='fancy_grid', numalign="center", showindex=row_id))
    try:
        input(F"\n{YL}-> Press Enter to go back to main menu...{R}\n")
        clear()
        main_menu_page()
    except SyntaxError:
        pass


def game_over():
    """
    This function is loaded when the user answers a question wrong and gives
    the option to play again. Uploads final score to Google Sheets.
    """
    while True:
        try:
            game_over_user = input(F"""{YL}Would you like to play again?
Type Y for yes or Q to go back to the main menu: {R}\n""").lower()
        except ValueError:
            clear()
            print(ASCII_GAME_OVER)
            sleep(0.2)
            print(F"\n{RD}Not a valid option, please enter Y or Q{R}\n")
        if game_over_user == "q":
            clear()
            main_menu_page()
        elif game_over_user == "y":
            clear()
            run_game()
        else:
            clear()
            print(ASCII_GAME_OVER)
            sleep(0.2)
            print(F"\n{RD}Not a valid option, please enter Y or Q{R}\n")


def run_game():
    """
    Run the main Quiz Game. Get question from question.toml.
    Checks user input (correct answer index 0).
    Displays next question if answer correct otherwise, game over.
    """
    global POINTS
    ascii_correct = GR + pyfiglet.figlet_format(
        "Correct!", font="rectangles", justify="center"
        ) + R
    ascii_winner = GD + pyfiglet.figlet_format(
        "Winner Winner!", font="rectangles", justify="center"
        ) + R
    questions = random.sample(list(QUESTIONS.items()), len(QUESTIONS))
    POINTS = 0
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(ASCII_BANNER)
        print(f"\n{YL}Question {num}:{R}")
        print(f"\n{question}\n")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f" {YL}{label.upper()}){R} {alternative}")
        if num_correct == 25:
            clear()
            print(ascii_winner)
            print(f"Well done {BL + USER_NAME + R}, you great Python master!")
            print(f"You scored {POINTS} points by answering all")
            print(f"{num_correct} questions correctly.\n")
            print(f"Another {GD}250{R} points will be added to your tally")
            print("for getting them all correctly.\n")
            POINTS += 250
            update_leaderboard()
            game_over()
            return

        while ((answer_label := input(f"\n{YL}Your selection? {R}\n").lower())
               not in labeled_alternatives):
            if answer_label == "q":
                clear()
                main_menu_page()
            else:
                clear()
                print(ASCII_BANNER)
                print(f"\n{YL}Question {num}:{R}")
                print(f"\n{question}\n")
                for label, alternative in labeled_alternatives.items():
                    print(f" {YL}{label.upper()}){R} {alternative}")
                sleep(0.2)
                print(f"\n{RD}Not a valid option!")
                print(
                    f"Please enter {','.join(labeled_alternatives).upper()}\
 or Q to quit to the main menu{R}""")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            clear()
            print(ascii_correct)
            POINTS += 10
            num_correct += 1
            correct_message = str(f"{GR}You have {POINTS} points.{R}")
            correct = correct_message.center(95)
            print(correct)
            sleep(2)
            clear()
        elif answer != correct_answer and num_correct == 0:
            clear()
            print(ASCII_GAME_OVER)
            print(f"\nOops {BL + USER_NAME + R}!")
            print(f"The correct answer is {correct_answer!r}, not {answer!r}")
            print("You scored no points this round.\n")
            game_over()
        else:
            clear()
            print(ASCII_GAME_OVER)
            print(f"The correct answer is {correct_answer!r},\
 not {answer!r}\n")
            print(f"\nNicely done {BL + USER_NAME + R}!")
            print(f"""You scored {POINTS} points by answering {num_correct}\
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
