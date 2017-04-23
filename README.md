* * *

                 ____       _                ____  _
                |  _ \ ___ | |__   ___      |  _ \| |__  
                | |_) / _ \| '_ \ / _ \     | | | | '_ \
                |  _ < (_) | |_) | (_) |    | |_| | |_) |  By: Vycktor Stark
                |_| \_\___/|_.__/ \___/     |____/|_.__/   Version: 4.0 - Facebook

                
* * *


## What is it?

Robot Db version 4.0 is a bot that uses the API "Facebook-Bot-API" written in Python, its structure was created in a simple way to show how easy it is to create a bot on facebook.

## Getting Started

These instructions provided you with information about this project to be used for development and testing purposes.

Well, you need to create a Facebook page.

The Facebook page is the "identity" of your bot, including the name and image that appears when someone speaks to you on Facebook Messenger.

If you are just creating a mannequin for your chatbot, it does not really matter what you name it or how you rank it. You can skip most of the setup steps. In order to communicate with your bot, people will have to go through your page.

Go to the Facebook developer's quick start page and click "Ignore and create the app ID" in the upper right corner. Then create a new Facebook application for your bot and give your application a name, category and contact email.

------
![https://blog.hartleybrody.com/wp-content/uploads/2016/06/create-fb-app-1024x604.png](https://blog.hartleybrody.com/wp-content/uploads/2016/06/create-fb-app-1024x604.png)

------

You'll see your new app ID in the upper right corner on the next page. Scroll down and click "Start" next to Messenger.

------
![https://blog.hartleybrody.com/wp-content/uploads/2016/06/setup-fb-messenger-app-1024x613.png](https://blog.hartleybrody.com/wp-content/uploads/2016/06/setup-fb-messenger-app-1024x613.png)

--------

Now you will configure your Facebook application. There are some things you need to fill out so that your chatbot stays connected, click on the authentication stream and you will receive a Page Access Token. Click the page access button to copy it to a clipboard and set it to the `config.py` file that is in the `utils` folder

------
![https://blog.hartleybrody.com/wp-content/uploads/2016/06/page-access-token-generation-1024x346.png](https://blog.hartleybrody.com/wp-content/uploads/2016/06/page-access-token-generation-1024x346.png)
------

This token will be used to authenticate your requests whenever you try to send a message or reply to someone.

To configure the request webhook for your Facebook page, you will need some bits of information:

Callback URL - The URL of your localhost

Token Verification - A secret value that will be sent to your bot to verify that the request comes from Facebook. Whatever the value set here, be sure to add it to the `config.py` file inside the `utils` folder in the `SENHA`

Signature Fields - This tells Facebook which messaging events you are interested in and want it to notify your webhook about. If you are not sure, just start with "messages" as you can change this later. Once you've set up your webhook, you'll need to sign up for the specific page for which you'd like to receive message notifications.

* * *

## Configuring bot

You should have your machine updated, having Python (3.5 +) and pip (8.1+) installed, plus some libs: objectjson, requests, simplejson.

What you need to do to install and use the project:

```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2

$ sudo apt-get update
$ sudo apt-get upgrade
## To install the libraries, just run run.sh and select option 5 or execute: 
$ sudo pip install -r requirements.txt
```

Cloning the repository:

```bash
$ git clone https://github.com/VycktorStark/DbRobot-Facebook-Python.git

```

## Initialization process

To start the bot, execute `cd DbRobot-Facebook-Python/ && pyhton3 main.py`. To stop the bot, press `Ctrl + c` twice.

* * *

## @DbRobot
