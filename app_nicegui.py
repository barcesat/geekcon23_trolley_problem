import os
from nicegui import ui
import random

# Set the paths to your folders A and B
folder_a_path = 'static/images/A/'
folder_b_path = 'static/images/B/'

def refresh_choices(random_index, image_files_a, image_files_b):
    # Check if there are images in both folders
    if not image_files_a or not image_files_b:
        print("No image files found in one or both of the specified folders.")
    else:
        # Randomly select an index
        print("selecting choice index: "+str(random_index))
        # Select the corresponding images
        selected_image_a = image_files_a[random_index]
        selected_image_b = image_files_b[random_index]
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

def display_index(random_index, selected_image_a, selected_image_b, text_a, text_b):
        grid.clear()
        with grid:
            with ui.interactive_image('static/images/A/'+selected_image_a, on_mouse=lambda: select_image('A')).style('max-height: 300px w-1/2').props('flat bordered') as image_holder_a:
                a_button = ui.button(text=text_a, on_click=lambda: select_image('A'), color="blue").classes('text-h3 w-full absolute-top justify-center')

            with ui.interactive_image('static/images/B/'+selected_image_b, on_mouse=lambda: select_image('B')).style('max-height: 300px w-1/2').props('flat bordered')  as image_holder_b:
                b_button = ui.button(text=text_b, on_click=lambda: select_image('B'), color="red").classes('text-h3 w-full absolute-top justify-center')

        with ui.row():
            ui.label('index: ' +str(random_index)).classes('vertical-bottom')

def select_image(selection):
    ui.notify(selection)
    print("user has selected: ",selection)
    random_index = random.randint(0, min(len(image_files_a), len(image_files_b)) - 1)
    selected_image_a, selected_image_b, text_a, text_b = refresh_choices(random_index, image_files_a, image_files_b)
    # Handle user's selection (e.g., load the selected image, update text, etc.)
    # Implement your logic here based on 'selected_image'
    return display_index(random_index, selected_image_a, selected_image_b, text_a, text_b)

if __name__ in {"__main__", "__mp_main__"}:
    # Get the list of image files from both folders
    image_files_a = [filename for filename in os.listdir(folder_a_path) if filename.endswith((".jpg", ".png"))]
    image_files_b = [filename for filename in os.listdir(folder_b_path) if filename.endswith((".jpg", ".png"))]
    print("got", str(len(image_files_a))," files on A")
    print("got", str(len(image_files_b))," files on B")
    with ui.row().classes('w-full justify-center'):
        ui.label('GeekCon 2023 Trolley Problem Game').classes('text-h4')
    ui.separator()
    first_random = random.randint(0, min(len(image_files_a), len(image_files_b)) - 1)
    print(first_random)
    selected_image_a, selected_image_b, text_a, text_b = refresh_choices(first_random, image_files_a, image_files_b)
    grid = ui.grid(columns=2)#.classes('w-full') #.classes('w-full absolute-center')
    display_index(first_random, selected_image_a, selected_image_b, text_a, text_b)
    
    with ui.row().classes('w-full justify-center'):
        # ui.label('GeekCon 2023 Trolley Problem Game').classes('text-h4')
        dark = ui.dark_mode()
        with ui.grid(columns=3).classes('absolute-bottom'):
            ui.label('Switch mode:')
            ui.button('Dark', on_click=dark.enable)
            ui.button('Light', on_click=dark.disable)
    ui.run(port=5000)