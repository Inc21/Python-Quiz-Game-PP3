# Introduction


![Game banner](/assets/images/quiz_game_banner.png)

This quiz is not like most quizzes out there, where you answer questions and by the end you get your score based on how many you got right or wrong. Basics of this game are simple. You get a question and four answers. Only one of the answer is correct. Where the "game" element comes in is when you answer that question. Answer correct and 10 points will be added to your account but answer incorrect and the game ends. Game records your name and score in database (Google sheet). Top 10 scores can be seen in High Scores section in main menu. Your goal is to get all 25 questions correct. Bonus will be added to your score and you can call yourself "Big deal in Python world"  

The game is Deployed on Code Institute mock terminal on Heroku. Live app can be found [here.](https://python-quiz-game-pp3.herokuapp.com/ "Python Quiz Game.")


![mockup](/assets/images/mockup.png)


# User Stories

### New User.

- I want to see clear instructions how to play this game.
- I want to be challenged and test my Python knowledge.
- I want to be able to see my score on the leaderboard and how it stacks up to the competition.

### Returning user.

- As a returning user, I want to start the game quick without having to go through how to play instructions again.
- As a returning user, I want to see and beat my previous score.

### Site owner objectives

- As a app creator, I want to provide fun learning experience.
- As a app creator, I want to add competitive element to the quiz.
- As a app creator, I want the app to be visually pleasant and readable.

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
- [Magic Mockups](http://magicmockups.com/) Responsive website mockup screenshot generator.

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

-  Option 3 in main menu. When opened it pulls most up-to-date leaderboard from Google sheets and displays top 10 highest scores. 
    - Data is stored in Google sheets and in order of entry. File is sorted by "score" or B column once pulled by the app. All valid tries will be recorded but only top 10 results will be displayed.

|   |  |
| - | - |
| ![High scores](/assets/images/high_scores.png) | ![Google Sheets](/assets/images/sheets.png)

### Exit

- Option 4 in main menu. When user chooses to leave the game nice thank you for playing message is printed on the screen.

![Exit message](/assets/images/exit_message.png)


### Features Left to Implement

- Different game modes Like "novice", "advanced" and "expert".
- Other common coding languages like JavaScript, html and others.
- Leaderboard top 10 fills very quickly with same users. would be great to add feature that records "user best score", not all attempts. 
    

 ## Testing

This app was developed on Dell desktop running windows 10. Testing was performed both locally and when deployed to Heroku. Using same computer and HP laptop running Windows 11 tried to "break" the program by entering random key entries. All my findings were corrected.
Also posted this project to Slack Peer code review and to my class page. One typo was reported back, which was fixed immediately.

### PEP8 Code Institute Python Linter Testing
- All clear, no errors found


![PEP8 Linter](/assets/images/py_lint.png)


### User Stories Testing

| Expectation | Solution |
| --- | --- |
| I want to see clear instructions how to play this game. | Game instruction section provided (option 2) in main menu. Also correct option examples provided when user makes a mistake. |
| I want to be challenged and test my Python knowledge. | 25 various Python related questions are provided. |
| I want to be able to see my score on the leaderboard and how it stacks up to the competition. | If the user is lucky to score enough point leaderboard section (option 3) in main menu is provided. |
| As a returning user, I want to start the game quick without having to go through how to play instructions again. | Option 1 in main menu will take user straight to the game and displays first question. |
| As a returning user, I want to see and beat my previous score. | Leaderboard section (option 3) in main menu is provided. |
| As a app creator, I want to provide fun learning experience. | If user answers question wrong, correct answer is provided for added learning |
| As a app creator, I want to add competitive element to the quiz. | Game records points and ends as soon as user answers question incorrectly hopefully making user want to come back and best their score. |
| As a app creator, I want the app to be visually pleasant and readable. | Ome colors, ascii text and line spacings were added to this terminal app to make it more user friendly |


### Welcome Screen Testing.
![](/assets/images/welcome_page_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
|  User hits enter without entering a name. | Invalid entry error is displayed along with the examples of correct entries.  | Working as expected | ![](/assets/images/invalid_name.png) |
| User enters name that is more than 10 characters | Invalid entry error is displayed along with the examples of correct entries.  ! | Working as expected | ![](/assets/images/invalid_name.png) |
| User enters just 1 character | Invalid entry error is displayed along with the examples of correct entries. | Working as expected | ![](/assets/images/invalid_name.png)|
| User enters a valid name. | App to load "Main Menu" page. | Working as expected |     |

### Main menu page Testing.
![]()
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |

### Game Instructions page Testing.
![]()
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |

### High scores page Testing.
![]()
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |



## Google Lighthouse testing 

| Text | Image |
| --- | --- |
| Google Chrome Lighthouse was used to test the performance of the app. Testing was performed in private browsing mode. | ![Google lighthouse](/assets/images/lighthouse.png) |


## Interesting bug or problems.

 Very new to Python language and most of this project was interesting problem that needed to be solved. Some standout problems listed below:
1. Python line too long. 
    - Researched this way more hours then I should have. Although PEP8 reports no errors, I think some of my solutions could be nicer and more readable. Also found a way to add line on vsCode window to show me when my line was getting too long in real time. This was a big help. Had about 20 Line too long errors on the first pass with CI linter.
2. Screen gets very cluttered looking with text history remaining on screen. User has to scroll to see important information.
    - That is another problem that took a big chunk of my available time. Ended up creating function called clear(). This clears the screen from old print statements for much better user experience.
3. Display and sort leaderboard imported from Google sheets.
    - Found sort() function after some very intense googling. That solved sorting leaderboard. After many trial and error ways to try to display that table on limited terminal window, tabulate was chosen for the job.
     

## Unfixed Bugs

No errors are reported by CI PEP8 Python Linter. vsCode is reporting one error and two warnings.
- 2 instances where I'm using the global statement. Pylint(W0603:global-statement)
    - Have USER_NAME and POINTS variables stated as global. Both are defined within function but will be used but are not redefined in other functions. I'm sure there is many more elegant ways to get around this. After spending many hours at this problem and as its not fatal error, decided to come back to it when possible.
- Name "tomllib" already defined (by an import)  [no-redef].
    - When researching a way to have questions stored in a separate file, went with [Real Pythons](https://realpython.com/python311-tomllib/) explanation to use TOML file. Used try/except statement as per their guide. try:import tomllib, except ModuleNotFoundError: import tomli as tomllib. By my understanding Python 3.11 uses tomllib and older versions of Python use TOML. This seems to be only error thats reported by mypy in vsCode. Very easily solvable by just deleting other instance of tomllib but to be backwards compatible and as it seems to create no bugs have decided to leave it as is.
    ...


## Deployment


### Deploy with Heroku

1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter name for your app. This name has to be unique. 
    - Heroku displays green tick is your app name is available.
4. In "choose a region" field choose either United States or Europe based on your location.
5. Click "Create app" button.
6. Next page, top center of the screen, select "Settings" tab. 
7. In "Config Vars" section, click on "Reveal config Vars" button.
8. In this section you need to enter you google sheets credentials. 
    1. Type name of credentials (CREDS in my case) file into "KEY" field.
    2. Open your IDE and find CREDS.json in your project files.
    3. Copy/paste everything in this file to "VALUE" field and click "Add" button.
9. Just below in "Buildpacks" section click on "Add buildback" button. Buildpacks have to be installed in this order.
    1. Click on "Python" button to select it and then "Save changes" button.
    2. Click again on "Add buildback" button.
    3. Click on "nodejs" button to select it and then "Save changes" button.
10. Go back to the top of the screen and select "Deploy" tab.
11. In "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on "Search" button. Find project repository in the list and click on "Connect" button.
    2. Scroll to the bottom of that page. Click on "Enable Automatic Deploys" button to update deploy also when you push new commit to GitHub.
    3. At teh very bottom of the page click on "Deploy Branch" button.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.


### Clone project 

- To clone this project.  
    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on "repositories".
    -  Find and click on "Python-Quiz-Game-PP3" repository.
    - In the repository page that opens, click on the 'Code' button.
    - Menu that opens make sure you are in the "local" tab, copy the link in "HTTPS".
    - paste that link into relevant section in your ide to clone repository.
        - CodeAnywhere. 
        - - Click on new "New Workspace" and paste that link to "Repository URL" field.
        - vsCode. 
        - - Select "File" and "New Window". In the middle of the page select "Clone Git Repositry...", 
        - - Paste that link into search box at the top of the screen and hit enter.
        - - Select local destination for repository files.
        

### Fork repository

- To fork this repository.
    - Open my [GitHub repository](https://github.com/Inc21/Python-Quiz-Game-PP3).
    - Click on the 'Fork' button on the top right of the screen.
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