import os
import numpy as np
import boto3
from flask import Flask, jsonify, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import re
import sys
from flask_cors import CORS
import logging

# Set TensorFlow logging level to suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Ensure the default encoding is set to UTF-8 (for Windows environments)
sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)
CORS(app)

# Disable Flask's debug logging
app.logger.setLevel(logging.WARNING)

# AWS S3 Configuration
s3 = boto3.client('s3')
S3_BUCKET = 'user-uploaded-images-penumonia'  # Replace with your actual S3 bucket name

# Load your trained pneumonia model
try:
    model = load_model('C:\\Sem V\\ICC_project\\best_pneumonia_cnn_model.h5')
    app.logger.info("Model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading model: {str(e)}")
    sys.exit(1)  # Exit the application if the model fails to load

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Function to upload file to S3
def upload_to_s3(file, filename):
    try:
        s3.upload_fileobj(file, S3_BUCKET, filename)
        app.logger.info(f"File uploaded to S3: {filename}")
        return f"File uploaded to S3: {filename}"
    except Exception as e:
        app.logger.error(f"Failed to upload to S3: {str(e)}")
        return jsonify({"error": f"Failed to upload to S3: {str(e)}"}), 500

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Sanitize the filename by checking for invalid characters
    filename = file.filename
    if not re.match(r'^[\w,\s-]+\.[A-Za-z]{3,4}$', filename):
        return jsonify({"error": "Invalid file name. Only alphanumeric characters, dashes, and underscores are allowed."}), 400

    try:
        # Process the image
        img = Image.open(file)
        img = img.resize((150, 150))  # Resize to the shape expected by your model
        img_array = np.array(img)

        # Ensure the image has the correct shape (150, 150, 3)
        if len(img_array.shape) == 2:  # Handle grayscale images by converting to RGB
            img_array = np.stack((img_array,)*3, axis=-1)

        img_array = img_array.astype('float32') / 255.0  # Normalize to [0,1]
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 150, 150, 3)
        
        # Upload the image to S3
        upload_to_s3(file, filename)

        # Make the prediction
        prediction = model.predict(img_array)
        result = 'Pneumonia Detected' if prediction[0][0] > 0.5 else 'No Pneumonia'

        return jsonify({'prediction': result})
    
    except Exception as e:
        app.logger.error(f"Error processing the image: {str(e)}")
        return jsonify({"error": f"Error processing the image: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
