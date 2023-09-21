import os

# Define the options from your table
'''
options_a = [
    "Pull a lever to one person",
    "Push a person off bridge",
    "Sacrifice yourself by jumping in front of trolley",
    "Five adults",
    "Five criminals",
    "Five doctors",
    "Five elderly individuals",
    "Five homeless people",
    "Five terminally ill individuals",
    "People from a different country",
    "People who are deaf and blind",
    "People who are unable to move",
    "People who are actively engaged in harmful activities",
    "People who are unaware of their surroundings",
    "People who have criminal records",
    "People from a different religious or cultural background",
    "People with no close family or friends",
    "People who are responsible for causing trolley to go out of control",
    "People who are strangers to you"
]

options_b = [
    "Do nothing, allowing trolley to five people",
    "Do nothing and allow trolley to five people",
    "Do nothing and let trolley to five people",
    "Five children",
    "Five innocent people",
    "Five firefighters",
    "Five young adults",
    "Five wealthy individuals",
    "Five healthy individuals",
    "People from your own country",
    "People with no disabilities",
    "People who can move but are unaware of danger",
    "Five innocent bystanders",
    "People who are paying full attention",
    "People with clean records",
    "People from your own religious or cultural background",
    "People with loving families",
    "Five innocent passengers",
    "People who are your friends or family"
]
'''
options_a = [
    "Replace your alarm clock with a rooster that crows at 4 AM every day",
    "Have your pet parrot narrate your life with constant commentary",
    "Be followed everywhere by a mariachi band playing upbeat music",
    "Have a magic TV remote that can pause real-life conversations",
    "Attend a dinner party with the world's most boring guests but free food",
    "Wear a chicken costume to every formal event for a year",
    "Have your phone autocorrect everything to emojis",
    "Live in a house filled with rubber ducks instead of furniture",
    "Replace your car horn with a loud quacking duck sound",
    "Have a personal stylist dress you like a different historical figure each day",
    "Use a keyboard that only types in emojis and Internet slang",
    "Be best friends with a stand-up comedian who roasts you daily",
    "Always speak in rhyming couplets",
    "Have a personal chef who only cooks bizarre food combinations",
    "Have your laugh sound like a famous celebrity's laugh",
    "Wear a suit made entirely of duct tape to formal events",
    "Have your food served on a surfboard with a live ukulele soundtrack",
    "Be followed by a paparazzi photographer documenting your daily life",
    "Replace your front door with a revolving door that plays circus music",
    "Have your email signature written in rhyming poetry"
]

options_b = [
    "Use a malfunctioning alarm clock that randomly changes its alarm time between 2 AM and 10 AM",
    "Have a GPS device narrate your every move, loudly and enthusiastically, even in your own home",
    "Have a clown follow you everywhere, offering unsolicited advice in rhymes",
    "Have a talking toilet that provides encouraging cheers after you flush",
    "Attend a karaoke night with politicians singing their campaign speeches",
    "Have your face appear on every billboard in your town for a month",
    "Have your phone speak in a different celebrity impersonation every day",
    "Live in a house decorated entirely with celebrity wax figures",
    "Replace your car's engine with a tiny lawnmower engine",
    "Have your wardrobe randomly disappear in public places, leaving you in your underwear",
    "Use a keyboard that types everything in rhyming couplets",
    "Be followed by a mascot who mimics your every move and expression",
    "Always narrate your life as if you're in a dramatic reality show",
    "Have a personal trainer who trains you using interpretive dance",
    "Have your sneeze sound like a famous politician's catchphrase",
    "Attend a gala where everyone wears pajamas and slippers",
    "Eat at a restaurant where waiters perform magic tricks instead of taking orders",
    "Be followed by a news anchor who provides live commentary on your actions",
    "Replace your front door with a giant red button that screams when pushed",
    "Have your voicemail message sung by a celebrity impersonator"
]

# Create pairs of text files
output_dir_A = "A"
output_dir_B = "B"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir_A):
    os.mkdir(output_dir_A)

if not os.path.exists(output_dir_B):
    os.mkdir(output_dir_B)

for i, (option_a, option_b) in enumerate(zip(options_a, options_b), 1):
    # Create file names for option A and option B
    option_a_filename = os.path.join(output_dir_A, f"{i+19}.txt")
    option_b_filename = os.path.join(output_dir_B, f"{i+19}.txt")

    # Write the content to the text files
    with open(option_a_filename, "w") as file_a, open(option_b_filename, "w") as file_b:
        file_a.write(option_a)
        file_b.write(option_b)

    print(f"Pair {i}:")
    print(f"Option A: {option_a_filename}")
    print(f"Option B: {option_b_filename}")
    print()

print("Text files created successfully.")
