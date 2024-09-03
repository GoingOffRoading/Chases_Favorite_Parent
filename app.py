from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

# Set the directory where the images are stored
IMAGE_DIR = os.path.join('static', 'images')

@app.route('/')
def index():
    # List all files in the image directory
    images = os.listdir(IMAGE_DIR)
    if not images:
        return "No images found in the directory.", 404
    
    # Pick a random image
    random_image = random.choice(images)
    
    return render_template('index.html', image=random_image)

@app.route('/images/<filename>')
def image(filename):
    # Serve the image file
    return send_from_directory(IMAGE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
