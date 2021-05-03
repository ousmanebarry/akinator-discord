# Akinator Discord Bot

## Table of Content

1. [Demo](#Demo)
2. [Description](#Description)
3. [Functionalities](#Functionalities)
4. [Installation Steps](#Installation-Steps)
5. [FAQ](#FAQ)
6. [Built With](#Built-With)
7. [License](#License)
8. [Author](#Author)
9. [Contact](#Contact)

## Demo 

[![image](https://user-images.githubusercontent.com/79618101/110070701-8789bb80-7d48-11eb-9df7-34fd1f912b8d.png)](https://imgur.com/a/LID2ynA)

Click on the image to take a look at the video or click [here](https://imgur.com/a/LID2ynA)

## Description

This is a bot which uses the [akinator.com](https://akinator.com/) API to enable users to play the akinator game directly on discord

## Functionalities

* Play akinator directly on discord
* Guess animals, objects and people

## Installation Steps

1. Go to [chrome webdriver](https://chromedriver.chromium.org/downloads) and donwload the correct webdriver for you version of chrome. 
2. **If you do not know your chrome version, you can find it** [here](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
3. During the installation process of Chrome WebDriver, remember the path where the exe file has been installed
4. Open the project with an IDE, inside the IDE built-in terminal write : `pip install -r requirements.txt`
5. Open **setup.py** and follow the instructions
6. You can now run the python code

## FAQ

* **Q**: **WHy is the bot is not registering my reaction?**

* **A**: Try to wait until the bot finishes adding all emojis before reacting. If that doesn't work, the game will end by itself in 45 seconds and you'll be able to play again


* **Q**: **Why isn't the bot sending the next question?**

* **A**: This is a problem with the akinator api, the only solution is to wait for the bot to end the game by itself in 45 seconds


* **Q**: **Why can't other people play while I'm playing?**

* **A**: Only one person can play at a time, I will update my code to allow more people to play at the same time later or you could take a look at the code and try to do it yourself if you can 


* **Q**: **Why did the game end suddenly?**

* **A**: Since only one person can play at a time, the game automatically ends after 45 seconds without user input to allow other people to play


* **Q**: **Why am I having problems running the bot?**

* **A**: You probably didn't follow the [installation steps](#Installation-Steps) well. Retry following the installation steps and if it still doesn't work try to [contact](#Contact) me

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - The IDE used
* [Akinator.py](https://pypi.org/project/akinator.py/) - Library for Akinator API
* [Python 3.9](https://www.python.org/) - The programming language used
* [Discord.py](https://discordpy.readthedocs.io/en/stable/) - A discord wrapper for Python
* [Chrome WebDriver](https://chromedriver.chromium.org/downloads) - The executable that replicates Google Chrome   

## License 

* This project is licensed under MIT License - see the [LICENSE.md](https://github.com/ousmanebarry/akinator-discord/blob/main/LICENSE) file for details

## Author

* This project was made by me and it is one of my first few Python projects

## Contact 

* If you're encountering any problems or would like to share some things I could improve this bot on, feel free to reach me on Discord at **Barry#0638** 
