#This is a funny game that shows the user the trolley problem\dillema
The trolley problem is a classic ethical thought experiment that presents a moral dilemma involving a runaway trolley headed towards a group of people. The participant must decide whether to take action that will divert the trolley, potentially sacrificing one person to save many, or do nothing and allow the trolley to harm multiple people. 
Some examples include:
A: Pull a lever to divert the trolley onto a track where it will hit one person.
B: Do nothing, allowing the trolley to hit five people on the current track.

A: Push a person off a bridge to block the trolley, sacrificing one life to save five.
B: Do nothing and allow the trolley to hit five people.

TODO:
- connect with arduino:
"A" - output command to control relay 1 (Toggle HIGH for 2 secs then LOW) 
"B" - output command to control relay 2 (Toggle HIGH for 2 secs then LOW) 
"R" - restart train (HIGH relay 3)
"S" - stop train (LOW relay 3)
"1" - choose track 1 (move servo to 0 degrees)
"2" - choose track 2 (move servo to 180 degrees)

To install:
pip install -r requirements.txt

To Run:
python3 app_nicegui.py