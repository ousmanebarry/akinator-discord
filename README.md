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

Click on the image to take a look at the video or click [here](https://streamable.com/efd0m2)

## Description

This is a bot which uses the [akinator.com](https://akinator.com/) API to enable users to play the akinator game directly on discord

## Functionalities

* Play akinator directly on discord
* Guess animals, objects and people
* Help command that shows how to play

## Installation Steps

1. Follow this [tutorial](https://www.writebots.com/discord-bot-token/) to get your **discord bot token** and invite that bot to your desired discord server 
2. Follow this [other tutorial](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/#:~:text=In%20Discord's%20settings%20menu%2C%20select,message%20sizes%2C%20and%20accessibility%20settings.&text=Scroll%20down%20to%20the%20bottom,the%20%E2%80%9CDeveloper%20Mode%E2%80%9D%20option.) to enable developer mode which will allow you to get the **channel id** of where you want the bot to be played in 
3. Once you have the **discord bot token** and **channel id**, navigate to the setup directory in this project and inside the setup file follow the instructions 
4. Open the project with an IDE, inside the IDE built-in terminal write : `pip install -r requirements.txt`
5. You can now run **main.py** and the bot should be up and running

## FAQ

* **Q**: **Why is the bot is not registering my reaction?**

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
