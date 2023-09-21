import cv2
import os
import msvcrt  # On Windows
# Set the paths to your folders A and B
folder_a_path = 'A'
folder_b_path = 'B'

# font = cv2.FONT_HERSHEY_SIMPLEX
font = cv2.FONT_HERSHEY_PLAIN
font_scale = 1
font_color = (0, 0, 0)  # Black - default
font_thickness = 2

# Maximum height for text to fit within the bottom quarter of the image
max_text_height = 100

# Line spacing (vertical offset) between lines of text
line_spacing = 10  # Adjust this value as needed

brightness_threshold = 100
# Function to calculate brightness in the bottom quarter of the image
def calculate_brightness(image):
    # Calculate the dimensions of the bottom quarter
    height, width, _ = image.shape
    bottom_quarter = image[3 * height // 4:, :, :]

    # Convert the bottom quarter to grayscale
    gray_bottom_quarter = cv2.cvtColor(bottom_quarter, cv2.COLOR_BGR2GRAY)

    # Calculate the average pixel value (brightness) of the bottom quarter
    brightness = cv2.mean(gray_bottom_quarter)[0]
    return brightness

# Function to calculate font scale based on image width
def calculate_font_scale(image_width, text, font, font_thickness):
    # Start with a large font scale
    font_scale = 2.0

    # Calculate the size of the text bounding box
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_width = text_size[0]

    # Reduce the font scale until the text fits within the image width
    while text_width > image_width:
        font_scale -= 0.1
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_width = text_size[0]
    return font_scale

try:
    while True:
        for filename in os.listdir(folder_a_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):  # Change the file extensions as needed
                image_a = cv2.imread(os.path.join(folder_a_path, filename))
                image_b = cv2.imread(os.path.join(folder_b_path, filename))

                # Read and display the text file
                text_file_pathA = os.path.join(folder_a_path, f"{os.path.splitext(filename)[0]}.txt")
                if os.path.exists(text_file_pathA):
                    with open(text_file_pathA, 'r') as file:
                        textA = file.read()
                
                # Read and display the text file
                text_file_pathB = os.path.join(folder_b_path, f"{os.path.splitext(filename)[0]}.txt")
                if os.path.exists(text_file_pathB):
                    with open(text_file_pathB, 'r') as file:
                        textB = file.read()
               
                # Split text into lines and display with line breaks
                linesA = textA.split('\n')
                linesB = textB.split('\n')

                # Calculate brightness of image
                brightness_a = calculate_brightness(image_a)
                brightness_b = calculate_brightness(image_b)

                # Resize images to 1/3 of their original size
                new_width = image_a.shape[1] // 3
                new_height = image_a.shape[0] // 3
                image_a = cv2.resize(image_a, (new_width, new_height))
                image_b = cv2.resize(image_b, (new_width, new_height))

                # Resize images to have the same dimensions
                max_height = max(image_a.shape[0], image_b.shape[0])
                max_width = max(image_a.shape[1], image_b.shape[1])
                image_a = cv2.resize(image_a, (max_width, max_height))
                image_b = cv2.resize(image_b, (max_width, max_height))

                font_scale_a = calculate_font_scale(image_a.shape[1], linesA[0], font, font_thickness)
                font_scale_b = calculate_font_scale(image_b.shape[1], linesA[1], font, font_thickness)

                if (textA):
                    # Choose text color based on brightness
                    if brightness_a < brightness_threshold:  # You can adjust this threshold
                        font_color_a = (255, 255, 255)  # White for dark images
                    else:
                        font_color_a = (0, 0, 0)  # Black for bright images
                    text_size_A = cv2.getTextSize(textA, font, font_scale, font_thickness)[0]
                    text_x_a = (image_a.shape[1] - text_size_A[0]) // 2
                    text_y_a = (image_a.shape[0] + text_size_A[1])*3 // 4
                    for i, line in enumerate(linesA):
                        cv2.putText(image_a, line, (text_x_a, text_y_a + i * text_size_A[1]), font, font_scale_a, font_color_a, font_thickness)
                        text_size_A[1]+1000

                if (textB):
                    if brightness_b < brightness_threshold:  # You can adjust this threshold
                        font_color_b = (255, 255, 255)  # White for dark images
                    else:
                        font_color_b = (0, 0, 0)  # Black for bright images
                    text_size_B = cv2.getTextSize(textB, font, font_scale, font_thickness)[0]
                    text_x_b = (image_b.shape[1] - text_size_B[0]) // 2
                    text_y_b = (image_b.shape[0] + text_size_B[1])*3 // 4
                    for i, line in enumerate(linesB):
                        cv2.putText(image_b, line, (text_x_b, text_y_b + i * text_size_B[1]), font, font_scale_b, font_color_b, font_thickness)
                        text_size_B[1]+100

                cv2.imshow("Images", cv2.hconcat([image_a, image_b]))
                key = cv2.waitKey(10000)  # Display for 10 seconds
                # Check for keyboard input (non-blocking)
                if msvcrt.kbhit():  # On Windows
                    key = msvcrt.getch().decode("utf-8")
                    if key == ord('A'):
                        cv2.imshow("Selected Image", image_a)
                        cv2.waitKey(0)
                    elif key == ord('B'):
                        cv2.imshow("Selected Image", image_b)
                        cv2.waitKey(0)

        cv2.destroyAllWindows()

except KeyboardInterrupt:
    print("Program terminated by user (Ctrl+C)")