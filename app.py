from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the paths to your folders A and B
folder_a_path = 'static/images/A/'
folder_b_path = 'static/images/B/'

@app.route('/')
def index():
    # Get the list of image files from both folders
    image_files_a = [filename for filename in os.listdir(folder_a_path) if filename.endswith((".jpg", ".png"))]
    image_files_b = [filename for filename in os.listdir(folder_b_path) if filename.endswith((".jpg", ".png"))]

    if not image_files_a or not image_files_b:
        return "No image files found in the specified folders."

    # Choose the first image from each folder
    image_a = image_files_a[0]
    image_b = image_files_b[0]

    # Read and display the text file for the selected image
    text_a_file_path = os.path.join(folder_a_path, os.path.splitext(image_a)[0] + ".txt")
    if os.path.exists(text_a_file_path):
        with open(text_a_file_path, 'r') as file:
            text_a = file.read()
    else:
        text_a = "No text available."
    
    # Read and display the text file for the selected image
    text_b_file_path = os.path.join(folder_b_path, os.path.splitext(image_b)[0] + ".txt")
    if os.path.exists(text_b_file_path):
        with open(text_b_file_path, 'r') as file:
            text_b = file.read()
    else:
        text_b = "No text available."

    return render_template('index.html', image_a=url_for('static', filename='images/A/' + image_a),
                           image_b=url_for('static', filename='images/B/' + image_b),
                           text_a=text_a, text_b=text_b)

@app.route('/select_image', methods=['POST'])
def select_image():
    selected_image = request.form.get('selected_image')

    # Handle user's selection (e.g., load the selected image, update text, etc.)
    # Implement your logic here based on 'selected_image'

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
