import os
import numpy as np
from flask import Flask, jsonify, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import io
import sys
import logging

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Ensure UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Initialize Flask app
app = Flask(__name__)
app.logger.setLevel(logging.WARNING)

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Load trained model
MODEL_PATH = 'C:\\Users\\Khushi Panchal\\Desktop\\PneumoniaDetection_Linux\\best_pneumonia_cnn_model.h5'
try:
    model = load_model(MODEL_PATH)
    app.logger.info("✅ Model loaded successfully.")
except Exception as e:
    app.logger.error(f"❌ Error loading model: {str(e)}")
    sys.exit(1)

# Check if file extension is valid
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home
@app.route('/')
def home():
    return render_template('index.html')

# Route: Predict
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected."}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Only .jpg, .jpeg, and .png are allowed."}), 400

    try:
        image = Image.open(file.stream).convert("RGB")
        image = image.resize((150, 150))
        image_array = np.array(image).astype('float32') / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)
        result = 'Pneumonia Detected' if prediction[0][0] > 0.5 else 'No Pneumonia'

        return jsonify({'prediction': result})

    except Exception as e:
        app.logger.error(f"❌ Error processing image: {str(e)}")
        return jsonify({"error": f"Error processing the image: {str(e)}"}), 500

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

