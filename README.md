# Introduction


![Game banner](/assets/images/quiz_game_banner.png)

This quiz is not like most quizzes out there, where you answer questions and by the end, you get your score based on how many you got right or wrong. The basics of this game are simple. You get a question and four answers. Only one of the answers is correct. Where the "game" element comes in when you answer that question. Answer correct and 10 points will be added to your account if the answer is incorrect the game ends. The game records your name and score in the database (Google sheet). The top 10 scores can be seen in the High Scores section in the main menu. Your goal is to get all 25 questions correct. Bonus will be added to your score and you can call yourself a "Big deal in the Python world"  

The game is Deployed on Code Institute mock terminal on Heroku. The live app can be found [here.](https://python-quiz-game-pp3.herokuapp.com/ "Python Quiz Game.")


![mockup](/assets/images/mockup.png)


# User Stories

### New User.

- I want to see clear instructions on how to play this game.
- I want to be challenged and test my Python knowledge.
- I want to be able to see my score on the leaderboard and how it stacks up to the competition.

### Returning user.

- As a returning user, I want to start the game quickly without having to go through how-to-play instructions again.
- As a returning user, I want to see and beat my previous score.

### Site owner objectives

- As an app creator, I want to provide a fun learning experience.
- As an app creator, I want to add a competitive element to the quiz.
- As an app creator, I want the app to be visually pleasant and readable.

# Design

## Look and feel

- As this game is developed with Python and designed to be run in the terminal, not too many design options are available. The main emphasis of this app is readability. 

## Colour
- To add a small bit of colour to text [Python colored](https://pypi.org/project/colored/ "Python colored.") module was used.

| Image | Color |
|---|---|
| ![dark_olive_green_2](/assets/images/dark_olive_green_2.png) | dark_olive_green_2 |
| ![light_red](/assets/images/light_red.png) | light_red |
| ![gold_3a](/assets/images/gold_3a.png) | gold_3a |
| ![light_yellow](/assets/images/light_yellow.png) | light_yellow |
| ![turquoise_2](/assets/images/turquoise_2.png) | turquoise_2 |

## Font

Arial is used for this app as per the Code Institute template. Added custom ascii headers using [Python pyfiglet](https://pypi.org/project/pyfiglet/0.7/ "Python pyfiglet.") module.
![Game banner](/assets/images/quiz_game_banner.png)


## Flowcharts
| Main game flow chart. | Quiz flow chart. |
|---|---|
| ![Python Quiz Game flow chart ](/assets/images/game_flow_chart.png) |  ![Quiz flow chart ](/assets/images/quiz_flow_chart.png) |


# Tools and technologies used

## Languages

- Python language and Python modules are listed below.
    - [random](https://docs.python.org/3/library/random.html) To randomize the order of the questions and answers.
    - [tomllib](https://docs.python.org/3/library/tomllib.html) Parse TOML file. Questions are stored in questions.toml file.
    - [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) To get the operating system name and clear the screen after some user options.
    - [time.sleep](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep) To add a delay after the user answers a question correctly.
    - [pyfiglet](https://pypi.org/project/pyfiglet/0.7/#:~:text=Pyfiglet%20is%20also%20a%20library,fonts%20from%20a%20zip%20archive.) To add some ascii text art.
    - [gspread](https://docs.gspread.org/en/v5.7.1/) Google Sheets to store "leaderboard"
    - [tabulate](https://pypi.org/project/tabulate/) To create and nicely display the leaderboard in the terminal.
    - [colored](https://pypi.org/project/colored/) Was used to add color to the terminal.



## Other tools and programs.

- [Lucid](https://lucid.co/) was used to create flow charts.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Google](https://www.google.ie/?gws_rd=ssl) sheets to store leaderboard.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where game is deployed using [Code Institute](https://codeinstitute.net/ie/) Python template.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.
- [Magic Mockups](http://magicmockups.com/) Responsive website mockup screenshot generator.

## Existing Features

### Welcome screen

- This is the first screen when the program is run. To continue user has to enter a name.

![Welcome screen](/assets/images/welcome_screen.png)  

### Main menu

- Once the user enters a valid name, the main menu screen is loaded. 

![Main menu](/assets/images/main_menu.png)  

### Play the quiz

- Option 1 - Play the Quiz.

![Game play](/assets/images/the_game.png) 

### Correct

- Displayed when the player answers a question correctly. This page is on delay. After 2 seconds new question is loaded.

![User answer is correct](/assets/images/correct.png)

### All 25 Correct

- Only displayed when the player answers all 25 questions correctly.

![Winner screen](/assets/images/winner_winner.png)

### Game Over

- Displayed when the player answers a question incorrectly. The correct answer is displayed for the added learning opportunity.

![User answer is incorrect](/assets/images/game_over.png)

### Game Over, no points

- Displayed when the player answers the first question incorrectly and has no points. The correct answer is displayed for the added learning opportunity.

![User first answer is correct](/assets/images/game_over_0.png)

### Instructions

- Option 2 in the main menu. Instructions on how to play the game and the game's end goal are displayed.

![Instructions](/assets/images/instructions.png)

### High Scores

-  Option 3 in the main menu. When opened it pulls the most up-to-date leaderboard from Google Sheets and displays the top 10 highest scores. 
    - Data is stored in Google Sheets and order of entry. The file is sorted by "score" or B column once pulled by the app. All valid tries will be recorded but only the top 10 results will be displayed.

|   |  |
| - | - |
| ![High scores](/assets/images/high_scores.png) | ![Google Sheets](/assets/images/sheets.png)

### Exit

- Option 4 in the main menu. When the user chooses to leave the game nice "thanks for playing" message is printed on the screen.

![Exit message](/assets/images/exit_message.png)


### Features Left to Implement

- Different game modes Like "novice", "advanced" and "expert".
- Other common coding languages like JavaScript, HTML and others.
- Leaderboard top 10 fills very quickly with the same users. would be great to add a feature that records the "user best score", not all attempts. 
    

 ## Testing

This app was developed on a Dell desktop running Windows 10. Testing was performed both locally and when deployed to Heroku. Using the same computer and HP laptop running Windows 11 tried to "break" the program by entering random key entries. All my findings were corrected.
Also posted this project to Slack Peer code review and my class page. One typo was reported back, which was fixed immediately.

### PEP8 Code Institute Python Linter Testing
- All clear, no errors found


![PEP8 Linter](/assets/images/py_lint.png)


### User Stories Testing

| Expectation | Solution |
| --- | --- |
| I want to see clear instructions on how to play this game. | Game instruction section provided (option 2) in the main menu. Also, correct option examples are provided when the user makes a mistake. |
| I want to be challenged and test my Python knowledge. | 25 various Python-related questions are provided. |
| I want to be able to see my score on the leaderboard and how it stacks up to the competition. | If the user is lucky to score enough point leaderboard section (option 3) in the main menu is provided. |
| As a returning user, I want to start the game quickly without having to go through how-to-play instructions again. | Option 1 in the main menu will take the user straight to the game and displays the first question. |
| As a returning user, I want to see and beat my previous score. | Leaderboard section (option 3) in the main menu is provided. |
| As an app creator, I want to provide a fun learning experience. | If the user answers a question wrong, the correct answer is provided for added learning |
| As an app creator, I want to add a competitive element to the quiz. | Game records points and ends as soon as the user answers a question incorrectly hopefully making the user want to come back and beat their score. |
| As an app creator, I want the app to be visually pleasant and readable. | Some colors, ascii text and line spacings were added to this terminal app to make it more user-friendly |


### Welcome Screen Testing.
![](/assets/images/welcome_page_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
|  User hits enter without entering a name. | Invalid entry error is displayed along with examples of correct entries.  | Working as expected | ![](/assets/images/invalid_user_none.png) |
| User enters name that is more than 10 characters | Invalid entry error is displayed along with the examples of correct entries.  ! | Working as expected | ![](/assets/images/invalid_user.png) |
| User enters just 1 character | Invalid entry error is displayed along with the examples of correct entries. | Working as expected | ![](/assets/images/invalid_user_1.png)|
| User enters a valid name. | App to load the "Main Menu" page. | Working as expected |     |

### Main menu page Testing.
![](/assets/images/menu_page_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters number "1" | Load Quiz page | Working as expected | |
| User enters number "2" | Load game instructions page | Working as expected | |
| User enters number "3" | Load high scores page | Working as expected | |
| User enters number "4" | Load goodbye message and exit the game | Working as expected | |
| User enters random wrong character or empty enter. | Display a red error message and show the correct options. | Working as expected | ![](/assets/images/invalid_meny_random.png) |

### Game Instructions page Testing.
![](/assets/images/instructions_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters random character or empty enter. | Game loads or goes back to the "main menu" page. | Working as expected | ![](/assets/images/instuctions_go_back.png) |

### High scores page Testing.
![](/assets/images/high_scores_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters random character or empty enter. | Game loads or goes back to the "main menu" page. | Working as expected | ![](/assets/images/high_scores_go_back.png) |

### Quiz page Testing.
![](/assets/images/quiz_page_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User answers question correctly by entering a, b, c or d | Display Correct message on points only for 2 seconds and then reloads new question. | Working as expected | ![](/assets/images/correct_small.png) |
| User answers the first question incorrectly. | Display "no points" game over page | Working as expected | ![](/assets/images/game_over_no_correct_small.png) |
| User answers question incorrectly by entering a, b, c or d. | Display game over page | Working as expected | ![](/assets/images/game_over_small.png) |
| User enters random character or empty enter. | Display a red error message and show the correct options. | Working as expected | ![](/assets/images/invalid_quiz_entry.png) |

### Game over page Testing.
![](/assets/images/game_over_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters random incorrect characters or empty "enter key". | Display error message and correct options | Working as expected | ![](/assets/images/invalid_quiz_entry.png) |
| User enters letter Q | Game loads main menu page | Working as expected | |
| User enters letter Y | Game loads game page from question 1 for same user | Working as expected | |

### Game over and "no points" page Testing.
![](/assets/images/game_over_no_correct_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User answers the first question wrong. | Display the "game over" page (will not update leaderboard) and play again message. | Working as expected | ![](/assets/images/quiz_play_again.png) | 
| User enters random incorrect characters or empty "enter key". | Display error message and correct options | Working as expected | ![](/assets/images/invalid_quiz_entry.png) |
| User enters letter Q | Game loads main menu page | Working as expected | |
| User enters letter Y | Game loads game page from question 1 for same user | Working as expected | |

### Exit game page Testing.
![](/assets/images/exit_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User selects number 4 "exit game". | Exit the application and display the "thanks for playing" message. |Working as expected | ![](/assets/images/exit_small.png) |


## Google Lighthouse testing 

| Text | Image |
| --- | --- |
| Google Chrome Lighthouse was used to test the performance of the app. Testing was performed in private browsing mode. | ![Google lighthouse](/assets/images/lighthouse.png) |


## Interesting bug or problems.

 Very new to Python language and most of this project was an interesting problem that needed to be solved. Some standout problems are listed below:
1. Python line too long. 
    - Researched this for way more hours than I should have. Although PEP8 reports no errors, I think some of my solutions could be nicer and more readable. Also found a way to add a line on the vsCode window to show me when my line was getting too long in real-time. This was a big help. Had about 20 "Line too long" errors on the first pass with the CI linter.
2. Screen gets very cluttered looking with text history remaining on screen. The user has to scroll to see important information.
    - That is another problem that took a big chunk of my available time. Ended up creating a function called clear(). This clears the screen from old print statements for a much better user experience.
3. Display and sort leaderboard imported from Google Sheets.
    - Found the sort() function after some very intense Googling. That solved sorting leaderboards. After many trial and error ways to try to display that table on a limited terminal window, tabulate was chosen for the job.
     

## Unfixed Bugs

No errors are reported by CI PEP8 Python Linter. vsCode is reporting one error and two warnings.
- 2 instances where I'm using the global statement. Pylint(W0603:global-statement)
    - Have USER_NAME and POINTS variables stated as global. Both are defined within the function but will be used but are not redefined in other functions. I'm sure there are many more elegant ways to get around this. After spending many hours on this problem and as it's not a fatal error, decided to come back to it when possible.
- Name "tomllib" already defined (by an import)  [no-redef].
    - When researching a way to have questions stored in a separate file, went with [Real Pythons](https://realpython.com/python311-tomllib/) explanation to use TOML file. Used try/except statements as per their guide. try: import tomllib, except ModuleNotFoundError: import tomli as tomllib. By my understanding, Python 3.11 uses tomllib and older versions of Python use TOML. This seems to be an error that's only reported by mypy in vsCode. Very easily solvable by just deleting other instances of tomllib but to be backwards compatible and as it seems to create no bugs have decided to leave it as is.
    ...


## Deployment


### Deploy with Heroku

1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your google sheets credentials. 
    1. Type the name of the credentials (CREDS in my case) file into the "KEY" field.
    2. Open your IDE and find CREDS.json in your project files.
    3. Copy/paste everything in this file to the "VALUE" field and click the "Add" button.
9. Just below in the "Buildpacks" section click on the "Add buildback" button. Buildpacks have to be installed in this order.
    1. Click on the "Python" button to select it and then the "Save changes" button.
    2. Click again on the "Add buildback" button.
    3. Click on the "nodejs" button to select it and then the "Save changes" button.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Enable Automatic Deploys" button to update the deploy also when you push a new commit to GitHub.
    3. At the very bottom of the page click on the "Deploy Branch" button.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.


### Clone project 

- To clone this project.  
    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on "repositories".
    -  Find and click on the "Python-Quiz-Game-PP3" repository.
    - In the repository page that opens, click on the 'Code' button.
    - Menu that opens make sure you are in the "local" tab, copy the link in "HTTPS".
    - paste that link into the relevant section in your ide to clone the repository.
        - CodeAnywhere. 
        - - Click on the "New Workspace" and paste that link to the "Repository URL" field.
        - vsCode. 
        - - Select "File" and "New Window". In the middle of the page select "Clone Git Repository...", 
        - - Paste that link into the search box at the top of the screen and hit enter.
        - - Select the local destination for repository files.
        

### Fork repository

- To fork this repository.
    - Open my [GitHub repository](https://github.com/Inc21/Python-Quiz-Game-PP3).
    - Click on the 'Fork' button on the top right of the screen.
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.

## Content

Questions gathered from the Internet:
-   [InterviewBit](https://www.interviewbit.com/)
-   [tutorialspoint](https://www.tutorialspoint.com/index.htm)
-   [sanfoundry](https://www.sanfoundry.com/1000-python-questions-answers/)


# Credits

Would like to say thanks to all for the support throughout the project.

- [Real Python](https://realpython.com/) Great site for some extra Python content. A lot of inspiration was taken from there.
- [Code Institute](https://codeinstitute.net/ie/) Love Sandwiches.
- [Slack community](https://slack.com/intl/en-ie/) and my classmates for tips and tricks and entertainment.
- My mentor Dick Vlaanderen who's continuously very supportive of me and very knowledgeable.