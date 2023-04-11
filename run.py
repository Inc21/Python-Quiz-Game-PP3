import random
from string import ascii_lowercase
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


print("\n Welcome to Python Quiz Game! \n")


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


def game_over():
    game_over_user = input("Would you like to play again? Type Y for yes or Q to quit: ").lower()
    if game_over_user == "q":
        exit()
    elif game_over_user == "y":
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

        while (answer_label := input("\nChoice? ").lower()) not in labeled_alternatives:
            if answer_label == "q":
                exit()
            print(f"Not a valid option, please enter {','.join(labeled_alternatives)} or q to quit")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            print("\n Correct! \n")
            points += 10
            num_correct += 1
        else:
            print( f"The answer is {correct_answer!r}, not {answer!r}\n")
            print("Game Over")
            print(f"\nYou scored {points} points by answering {num_correct} questions correctly.\n")
            game_over()


def main():
    """
    Run all program functions.
    """
    run_game()


main()
