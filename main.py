import os
import random
from flask import Flask, render_template

app = Flask(__name__)

# Replace 'YOUR_IMAGE_DIRECTORY_PATH' with the path to your local image directory
IMAGE_DIRECTORY_PATH = 'YOUR_IMAGE_DIRECTORY_PATH'

@app.route('/')
def index():
    # Get a random image file from the local directory
    image_path = get_random_image_path()
    return render_template('index.html', image_path=image_path)

def get_random_image_path():
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(IMAGE_DIRECTORY_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if image_files:
        # Get a random image file path
        random_image = random.choice(image_files)
        image_path = os.path.join(IMAGE_DIRECTORY_PATH, random_image)
        return image_path
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
