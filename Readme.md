# The Trolley Problem game
This is a fun game based on the famous the trolley problem\dillema.

The trolley problem is a classic ethical thought experiment that presents a moral dilemma involving a runaway trolley headed towards a group of people. 

The participant must decide whether to take action that will divert the trolley, potentially sacrificing one person to save many, or do nothing and allow the trolley to harm multiple people.

Some examples include:

**A:** Pull a lever to divert the trolley onto a track where it will hit one person you know.

**B:** Do nothing, allowing the trolley to hit ten people on the current track.


**A:** Pull a lever to divert the trolley onto a track where it will hit two terminally ill people.

**B:** Do nothing, allowing allow the trolley kill one healthry person.

## Geekcon 2023

During the annual crazy GeekCon 2023 Hackathon taking place September 21-23st @ Sdot-Yam in ISrael our team has developed this game with some sdditions:

1. Part of the dillemas were broght in from speaking to ChatGPT
2. To illustrate some dillemas, we generated images using the Stable Diffusion engine.
3. The game has connected a real toy train and controlled its track changes. 

The team members were:
1. Ziv Barcesat
2. Tal Raindel
3. Michael Lev-ari Layosh
4. Yuval Raindel
5. Guy Sheffer

## Software
The game is written in python that utilizes the speedy NiceGUI library to create a web UI.
The communication with the hardware is done using serial interface. 

To Install (assuming you have installed python on your PC):
pip install -r requirements.txt

To Run:
python3 app_nicegui.py

(This will auto load the game in the web browser at: 127.0.0.1:5000)
## Hardware
For this project we purchased a [model train toy from amazon](https://www.amazon.com/Electric-Holidays-Christmas-Experience-Accessories/dp/B08818K84M?ref_=ast_sto_dp).

We designed and 3D printed mounting for 9g servo motors to fit on the levers to change the routes and for a bumper that stops the train.

In order to do it we took an Arduino Uno controller board and connected the servos to it.

The code is written and compiled using the platform.io development platform.

Screenshot from the game:
![img](Screenshot.jpg 'Screenshot')

Photos from the display:
![img](display.jpg 'display')
![img](display2.jpg 'display')
![img](display3.jpg 'display')

The train set
![img](trainset.jpg 'trainset')