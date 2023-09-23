import os
from nicegui import ui
import random
from trolley_control import ArduinoController


# Set the paths to your folders A and B
folder_a_path = 'static/images/A/'
folder_b_path = 'static/images/B/'
descision_timeout_increment = 0.1
descision_timeout = 10.0
user_has_selected = False
current_selection = "NONE"
current_selection_text = "NONE"

def update_timer():
    global user_has_selected
    slider.set_value((slider.value + 0.1) % 10.1)
    # print (slider.value)
    
    if slider.value >= 10.0 and user_has_selected == True: #timer out - restart
        print("time up - selection has been made")
        slider.set_value(0.0)
        countdown.deactivate()
        countdown.activate()
        user_has_selected = False
        select_image(current_selection,current_selection_text)
    
    elif slider.value >= 10.0 and user_has_selected == False: #timeout
        print("timeout")
        slider.set_value(0.0)
        countdown.deactivate()
        select_image("NONE", "NONE")

def make_selection(selection, selection_text):
    global user_has_selected, current_selection, current_selection_text
    current_selection = selection
    current_selection_text = selection_text
    user_has_selected = True


def refresh_choices(index, image_files_a, image_files_b):
    # Check if there are images in both folders
    if not image_files_a or not image_files_b:
        print("No image files found in one or both of the specified folders.")
    else:
        # Randomly select an index
        print("selecting choice index: "+str(index))
        # Select the corresponding images
        selected_image_a = image_files_a[index]
        selected_image_b = selected_image_a
        print("A: ", selected_image_a, "B: ", selected_image_b)

        # Read and display the text file for the selected image
        text_a_file_path = os.path.join(folder_a_path, os.path.splitext(selected_image_a)[0] + ".txt")
        if os.path.exists(text_a_file_path):
            with open(text_a_file_path, 'r') as file:
                text_a = file.read()
        else:
            text_a = "No text available."
        
        # Read and display the text file for the selected image
        text_b_file_path = os.path.join(folder_b_path, os.path.splitext(selected_image_b)[0] + ".txt")
        if os.path.exists(text_b_file_path):
            with open(text_b_file_path, 'r') as file:
                text_b = file.read()
        else:
            text_b = "No text available."
        
        return selected_image_a, selected_image_b, text_a, text_b

def display_index(index, selected_image_a, selected_image_b, text_a, text_b):
    grid.clear()
    with grid:
        with ui.interactive_image('static/images/A/'+selected_image_a, on_mouse=lambda: make_selection('A', text_a)).props('flat bordered') as image_holder_a:
            a_button = ui.button(text=text_a, on_click=lambda: make_selection('A', text_a), color="blue").classes('text-h3 w-full absolute-top justify-center')

        with ui.interactive_image('static/images/B/'+selected_image_b, on_mouse=lambda: make_selection('B', text_b)).props('flat bordered')  as image_holder_b:
            b_button = ui.button(text=text_b, on_click=lambda: make_selection('B', text_b), color="red").classes('text-h3 w-full absolute-top justify-center')

        with ui.row():
            ui.label('index: ' +str(index)).classes('vertical-bottom')

def select_image(selection, selection_text):
    global user_has_selected
    random_index = random.randint(0, max(len(image_files_a), len(image_files_b)) - 1)
    selected_image_a, selected_image_b, text_a, text_b = refresh_choices(random_index, image_files_a, image_files_b)
    if selection == "NONE":
        ui.notify("Abstention is just as worse as taking an action!", type='negative',classes='multi-line-notification')
        countdown.deactivate()
        countdown.activate()
        return display_index(random_index, selected_image_a, selected_image_b, text_a, text_b)
    
    elif selection == "A":
        ui.notify("You have selected: "+ selection_text, multi_line=True, classes='multi-line-notification')
        # user_has_selected = True
    
    elif selection == "B":
        ui.notify("You have selected: "+ selection_text, multi_line=True, classes='multi-line-notification')
        # user_has_selected = True
    
    print("user has selected: ",selection, selection_text)

    # Implement your logic here based on 'selected_image'
    if arduino.port_opened_successfully:
        try:
            if selection == "A":
                response = arduino.choose_track_1()
            elif selection == "B":
                response = arduino.choose_track_2()
            print("Arduino Response:", response)
        except:
            print("Arduino is Disconnected!")
            ui.notify("Trolley is Disconnected!", type='negative')
    # Handle user's selection (e.g., load the selected image, update text, etc.)
    
    return display_index(random_index, selected_image_a, selected_image_b, text_a, text_b)

def new_game_time():
    data = arduino.read_response()
    if data == "out station":
        print("***************************** NEW GAME ****************************")
        return True
    else:
        return False

if __name__ in {"__main__", "__mp_main__"}:
    arduino = ArduinoController(port="COM3")
    if arduino.port_opened_successfully:
        print("Arduino is Connected!")
    else:
        print("Arduino is Disconnected!")
    try:
        ui.html('<style>.multi-line-notification { font-size: 40px; white-space: pre-line; }</style>')
        # Get the list of image files from both folders
        image_files_a = [filename for filename in os.listdir(folder_a_path) if filename.endswith((".jpg", ".png"))]
        image_files_b = [filename for filename in os.listdir(folder_b_path) if filename.endswith((".jpg", ".png"))]
        print("got", str(len(image_files_a))," files on A")
        print("got", str(len(image_files_b))," files on B")
        first_random = random.randint(0, min(len(image_files_a), len(image_files_b)) - 1)
        print(first_random)
        
        # Build the UI
        with ui.row().classes('w-full justify-center'):
            ui.label('GeekCon 2023 Trolley Problem Game').classes('text-h4')
        ui.separator()
        slider = ui.slider(min=0, max=10, value=0)
        user_has_selected = False
        countdown = ui.timer(descision_timeout_increment, lambda: update_timer())#select_image('NONE'))#, once=True)
        
        selected_image_a, selected_image_b, text_a, text_b = refresh_choices(first_random, image_files_a, image_files_b)

        grid = ui.grid(columns=2).style("grid-auto-columns: auto; grid-auto-columns: auto; align-self: center;")
        display_index(first_random, selected_image_a, selected_image_b, text_a, text_b)
        
        with ui.row().classes('w-full justify-center'):
            dark = ui.dark_mode()
            with ui.grid(columns=3).classes('absolute-bottom'):
                ui.label('Switch mode:')
                ui.button('Dark', on_click=dark.enable)
                ui.button('Light', on_click=dark.disable)
        
        if arduino.port_opened_successfully:
            new_game = new_game_time()
            if new_game:
                print("new game")
                new_random = random.randint(0, min(len(image_files_a), len(image_files_b)) - 1)
                refresh_choices(new_random, image_files_a, image_files_b)
        else:
            countdown.activate()
        # print("SGDFGSD")
        
            # countdown.activate()

        
        ui.run(port=5000)

    except KeyboardInterrupt:
            print("Exiting...")
            arduino.close_connection()