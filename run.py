import gspread
from google.oauth2.service_account import Credentials
from string import ascii_lowercase

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('phyton_quiz_leaderboard')


print("\n Welcome to Python Quiz Game! \n")


QUESTIONS =  {
    "How is a code block indicated in Python?": [
        "Indentation", "Brackets", "Key", "None of the above"
    ],
    "What is the maximum length of a Python identifier?": [
        "No fixed lenght is specified", "32", "16", "128"
    ],
    "Which of the following concepts is not a part of Python?": [
        "Pointers", "Loops", "Dynamic Typing", "All the above"
    ],
    "Which of the following statements are used in Exception Handling in Python?": [
        "All of the above", "try", "except", "finally"   
    ],
}


for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}")
    correct_answer = alternatives[0]
    labled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labled_alternatives.items():
        print(f" {label}) {alternative}")

    answer_label = input("\nChoice? ").lower()
    answer = labled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("\n Correct! \n")   
    else:
        print( f"The answer is {correct_answer!r}, not {answer!r}\n")
        print("Game Over")
        exit()     



def main():
    """
    Run all program functions.
    """
    print("Works")
    
# main()