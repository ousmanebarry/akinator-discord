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

This is a automated program for the website [typeracer.com](https://play.typeracer.com/) made with the use of Python that automatically plays normal games on the website. It is a simple automating script that uses selenium and pyautogui. 

## Functionalities

* Automatically logs in to a [typeracer.com](https://play.typeracer.com/) account 
* Automatically plays normal games
* Automatically keeps playing the number of times asked by the user

## Installation Steps

1. Go to [chrome webdriver](https://chromedriver.chromium.org/downloads) and donwload the correct webdriver for you version of chrome. 
2. **If you do not know your chrome version, you can find it** [here](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
3. During the installation process of Chrome WebDriver, remember the path where the exe file has been installed
4. Open the project with an IDE, inside the IDE built-in terminal write : `pip install -r requirements.txt`
5. Open **setup.py** and follow the instructions
6. You can now run the python code

## FAQ

* **Q**: **How do I change the bot typing speed?**

* **A**: In line 35 of the **main.py** file, you can play with the number inside interval. _PS : I recommend keeping it at the current speed as it seems to be the optimal one_


* **Q**: **Why doesn't the bot type faster?**

* **A**: Pyautogui is sometimes too fast and [typeracer.com](https://play.typeracer.com/) seems to have limitations as to how fast you can type using pyautogui. _PS : I'm looking for a work-around_


* **Q**: **What average wpm can I except with the current configuration?**

* **A**: You can except an average of around 100wpm to 115 wmp


* **Q**: **Why does the bot not get past the login page?**

* **A**: Make sure your account is verified and you put in the correct login informations


* **Q**: **Why am I having problems running the bot?**

* **A**: You probably didn't follow the [installation steps](#Installation-Steps) well. Retry following the installation steps and if it still doesn't work try to [contact](#Contact) me

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - The IDE used
* [Akinator.py](https://pypi.org/project/akinator.py/) - Library for Akinator API
* [Python 3.9](https://www.python.org/) - The programming language used
* [Discord.py](https://discordpy.readthedocs.io/en/stable/) - A discord wrapper for Python
* [Chrome WebDriver](https://chromedriver.chromium.org/downloads) - The executable that replicates Google Chrome   

## License 

This project is licensed under MIT License - see the [LICENSE.md](https://github.com/ousmanebarry/typeracer-bot/blob/main/LICENSE) file for details

## Author

* This project was made by me. It is one of my first few Python projects and I will add more functionalities to this as time goes 

## Contact 

* If you're encountering any problems or would like to share some things I could improve this bot on, feel free to reach me on Discord at **Barry#0638** 
