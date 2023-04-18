# Introduction


![Game banner](/assets/images/quiz_game_banner.png)

This quiz is not like most quizzes out there, where you answer questions and by the end you get your score based on how many you got right or wrong. Basics of this game are simple. You get a question and four answers. Only one of the answer is correct. Where the "game" element comes in is when you answer that question. Answer correct and 10 points will be added to your account but answer incorrect and the game ends. Game records your name and score in database (Google sheet). Top 10 scores can be seen in High Scores section in main menu. Your goal is to get all 25 questions correct. Bonus will be added to your score and you can call yourself "Big deal in Python world"  

The game is Deployed on Code Institute mock terminal on Heroku. Live app can be found [here.](https://python-quiz-game-pp3.herokuapp.com/ "Python Quiz Game.")


![mockup](/assets/images/mockup.png)


# User Stories

### New User.

- I want to see instructions how to play this game.
- I want to be challenged and test my Python knowledge.
- I want to be able to see my score on the leaderboard and how it stacks up to the competition.

### Returning user.

- As a returning user, I want to start the game quick without having to go through how to play instructions again.
- As a returning user, I want to see and beat my previous score.

### Site owner objectives

- As a app creator, I want to provide fun learning experience.
- As a app creator, I want to add competitive element to the quiz.
- As a app creator, I want to be visually pleasant and readable.

# Design

## Look and feel

- As this game is developed with Python and designed to be run in the terminal, not to many design options available. Main emphasis in this app is readability. 

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

Arial is used for this app as per Code Institute template. Added custom ascii headers using [Python pyfiglet](https://pypi.org/project/pyfiglet/0.7/ "Python pyfiglet.") module.
![Game banner](/assets/images/quiz_game_banner.png)


## Flowcharts
| Main game flow chart. | Quiz flow chart. |
|---|---|
| ![Python Quiz Game flow chart ](/assets/images/game_flow_chart.png) |  ![Quiz flow chart ](/assets/images/quiz_flow_chart.png) |


# Tools and technologies used

## Languages

- Python language and Python modules listed below.
    - [random](https://docs.python.org/3/library/random.html) To randomize order of the questions and answers.
    - [tomllib](https://docs.python.org/3/library/tomllib.html) Parse TOML file. Questions are stored in questions.toml file.
    - [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) To get operating system name and clear the screen after some user options.
    - [time.sleep](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep) To add delay after user answers question correctly.
    - [pyfiglet](https://pypi.org/project/pyfiglet/0.7/#:~:text=Pyfiglet%20is%20also%20a%20library,fonts%20from%20a%20zip%20archive.) To add some ascii text art.
    - [gspread](https://docs.gspread.org/en/v5.7.1/) Google Sheets to store "leaderboard"
    - [tabulate](https://pypi.org/project/tabulate/) To create and nicely display leaderboard in terminal.
    - [colored](https://pypi.org/project/colored/) Was used to add color to terminal.



## Other tools and programs.

- [Lucid](https://lucid.co/) was used to create flow charts.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Google](https://www.google.ie/?gws_rd=ssl) sheets to store leaderboard.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where game is deployed using [Code Institute](https://codeinstitute.net/ie/) Python template.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.
- [Website Mockup Generator](https://websitemockupgenerator.com/) Responsive website mockup screenshot generator.

## Existing Features

### Welcome screen

- This is the fist screen when program is run. To continue user has to enter a name.

![Welcome screen](/assets/images/welcome_screen.png)  

### Main menu

- Once user enters valid name, main menu screen is loaded. 

![Main menu](/assets/images/main_menu.png)  

### Play the quiz

- Option 1 - Play the Quiz.. 

![Game play](/assets/images/the_game.png) 

### Correct

- Displayed when player answers question correctly. This page is on delay. After 2 seconds new question is loaded.

![User answer is correct](/assets/images/correct.png)

### All 25 Correct

- Only displayed when player answers all 25 questions correct.

![Winner screen](/assets/images/winner_winner.png)

### Game Over

- Displayed when player answers question incorrectly. Correct answer is displayed for added learning opportunity.

![User answer is incorrect](/assets/images/game_over.png)

### Game Over 0 points

- Displayed when player answers first question incorrectly and has no points. Correct answer is displayed for added learning opportunity.

![User first answer is correct](/assets/images/game_over_0.png)

### Instructions

- Option 2 in main menu. Instructions how to play the game and game end goal is displayed.

![Instructions](/assets/images/instructions.png)

### High Scores

- Option 3 in main menu. When opened it pulls most up-to-date leaderboard from Google sheets and displays top 10 highest scores.  

![High scores](/assets/images/high_scores.png)

### Exit

- Option 4 in main menu. When user chooses to leave the game nice thank you for playing message is printed on the screen.

![Exit message](/assets/images/exit_message.png)


### Features Left to Implement

- Different game modes Like "novice", "advanced" and "expert".
- Other common coding languages like JavaScript, html and others.
- Leaderboard top 10 fills very quickly with same users. would be great to add feature that records "user best score", not all attempts. 
    

## Testing

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### User Stories Testing

| Expectation | Result | Images |
| --- | --- | --- |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquam diam. In semper aliquet mi eget dignissim. Etiam pharetra elit id interdum accumsan. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquam diam. In semper aliquet mi eget dignissim. Etiam pharetra elit id interdum accumsan. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquam diam. In semper aliquet mi eget dignissim. Etiam pharetra elit id interdum accumsan. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquam diam. In semper aliquet mi eget dignissim. Etiam pharetra elit id interdum accumsan. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |     |

### Link testing

| Action | Expected Result | Actual Result |
| --- | --- | --- |
|     |     | Working as expected |


###  Manual Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
|     |     | Working as expected |     |
|     |     | Working as expected |     |
|     |     | Working as expected |     |
|     |     | Working as expected |     |
|     |     | Working as expected. |     |


## Google Lighthouse testing 

| Text | Image |
| --- | --- |
| Google Chrome Lighthouse was used to test the performance of the app. Testing was performed in private browsing mode. | ![Google lighthouse](/assets/images/lighthouse.png) |




Desktop

Mobile

## Interesting bug or problems.

    -   
    

## Unfixed Bugs

No errors are reported by CI PEP8 Python Linter. Vs Code is reporting one error and two warnings.
- 2 instances where I'm using the global statement. Pylint(W0603:global-statement)
    - Have USER_NAME and POINTS variables stated as global. Both are defined within function but will be used but are not redefined in other functions. I'm sure there is many more elegant ways to get around this. After spending many hours at this problem and as its not fatal error, decided to come back to it when possible.
- Name "tomllib" already defined (by an import)  [no-redef].
    - When researching a way to have questions stored in a separate file, went with [Real Pythons](https://realpython.com/python311-tomllib/) explanation to use TOML file. Used try/except statement as per their guide. try:import tomllib, except ModuleNotFoundError: import tomli as tomllib. By my understanding Python 3.11 uses tomllib and older versions of Python use TOML. This seems to be only error thats reported by mypy in vsCode. Very easily solvable by just deleting other instance of tomllib but to be backwards compatible and as it seems to create no bugs have decided to leave it as is.
    ...


## Deployment

### Deploy with GitHub Pages.

The steps to deploy are as follows:

    - On my [GitHub](https://github.com/Inc21) profile page, top center of the screen click on repositories.
    - Click on 
    - In the ##### repository, navigate to the Settings tab.
    - Menu list on the left of the screen, navigate to the pages tab.
    - From the GitHub pages, branch section drop-down menu, select the main Branch and hit the save button.
    - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - [here](https://https:// "https://https://")

### Local Deployment

The steps to deploy are as follows:

    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on repositories.
    - Click on
    - In the tic-tac-toe-pp2 repository, click on the 'Code' button.
    - Menu that opens make sure you are in the "local" tab, copy the link in "HTTPS".
    - on a Windows machine, open the command prompt (press windows+R to open the "Run" box. Type "cmd" on then click ok).
    - In cmd type "git clone" and paste the link you copied earlier (ctrl+V). Example: git clone

### Fork repository

    - To fork a repository that is not yours
    - Click on the 'Fork' button on the top right of the screen
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.

## Content

Questions gathered from the internet:
-   [InterviewBit](https://www.interviewbit.com/)
-   [tutorialspoint](https://www.tutorialspoint.com/index.htm)
-   [sanfoundry](https://www.sanfoundry.com/1000-python-questions-answers/)


# Credits

Would like to say thanks to all for the support throughout the project.

- [Real Python](https://realpython.com/) Great site for some extra python content. Lot of inspiration was taken from there.
- [Code Institute](https://codeinstitute.net/ie/) Love Sandwiches.
- [Slack community](https://slack.com/intl/en-ie/) and my classmates for tips and tricks and entertainment.
- My mentor Dick Vlaanderen who is continuously very supportive of me and very knowledgeable.