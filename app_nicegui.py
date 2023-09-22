# from flask import Flask, render_template, request, redirect, url_for
import os
from nicegui import ui
import random
# app = Flask(__name__)

# Set the paths to your folders A and B
folder_a_path = 'static/images/A/'
folder_b_path = 'static/images/B/'



# @app.route('/')
def index():
    # Get the list of image files from both folders
    image_files_a = [filename for filename in os.listdir(folder_a_path) if filename.endswith((".jpg", ".png"))]
    image_files_b = [filename for filename in os.listdir(folder_b_path) if filename.endswith((".jpg", ".png"))]

    # Check if there are images in both folders
    if not image_files_a or not image_files_b:
        print("No image files found in one or both of the specified folders.")
    else:
        # Randomly select an index
        random_index = random.randint(0, min(len(image_files_a), len(image_files_b)) - 1)

        # Select the corresponding images
        selected_image_a = image_files_a[random_index]
        selected_image_b = image_files_b[random_index]

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


        with ui.grid(columns=2):
            ui.label(text_a)
            ui.label(text_b)

            with ui.interactive_image('static/images/A/'+selected_image_a).style('width: 75%'):
                # ui.button(on_click=lambda: ui.notify('A'), icon='thumb_up') \
                #     .props('flat fab color=white') \
                #     .classes('absolute bottom-0 left-0 m-2')
                ui.label(text_a).classes('absolute-top text-subtitle1 text-center')

            # ui.image('static/images/B/'+selected_image_b)
            
            with ui.interactive_image('static/images/B/'+selected_image_b).style('width: 75%'):
                # ui.button(on_click=lambda: ui.notify('B'), icon='thumb_up') \
                #     .props('flat fab color=white') \
                #     .classes('absolute bottom-0 left-0 m-2')
                ui.label(text_b).classes('absolute-top text-subtitle1 text-center')
        
        
        dark = ui.dark_mode()
        ui.label('Switch mode:')
        ui.button('Dark', on_click=dark.enable)
        ui.button('Light', on_click=dark.disable)
    # return render_template('index.html', image_a=url_for('static', filename='images/A/' + image_a),
                        #    image_b=url_for('static', filename='images/B/' + image_b),
                        #    text_a=text_a, text_b=text_b)

# @app.route('/select_image', methods=['POST'])
def select_image():
    # selected_image = request.form.get('selected_image')

    # Handle user's selection (e.g., load the selected image, update text, etc.)
    # Implement your logic here based on 'selected_image'

    return redirect(url_for('index'))

if __name__ in {"__main__", "__mp_main__"}:
    # app.run(debug=True)
    # ui.label('Hello NiceGUI!')
    ui.run(port=5000)
    index()