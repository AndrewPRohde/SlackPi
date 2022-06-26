SlackPi

SlackPi is designed to monitor your Slack workspace for activity and display all incoming messages to a 1602 LCD display.

Main.py will take the returned data from SlackHandler and present it to PiHandler to be displayed

PiHandler will build the class/functions that display text on the LCD. It will also control the LED notification lights and the notification sound

SlackHandler will utilize the Slack API to monitor the chosen workspace for activity. It will also strip the relevant information and present it to Main.py to be displayed