# Pneumonia Detection from Chest X-Ray Images using Deep Learning

This project is a complete pipeline for **detecting pneumonia from chest X-ray images** using **Convolutional Neural Networks (CNNs)** with automated **hyperparameter tuning** via **Keras Tuner**, and a **Flask web application** to allow real-time predictions from user-uploaded images.

The core objective is to build a medical image classifier that distinguishes between **normal** lungs and those affected by **pneumonia**, enabling faster preliminary screening which can assist healthcare professionals.

This project demonstrates not only **deep learning model building and optimization**, but also how to **deploy the model** into a usable web service for real-world interaction.

---

## Project Structure

```
Pneumonia-Detection/
│
├── Backend/
│   ├── requirements.txt          # Lists all required Python packages for backend
│   ├── cnn_model.py              # Code for training the CNN model
│   └── ...
│
├── Frontend/
│   ├── app2.py                   # Flask application that serves the frontend and handles requests
│   ├── index.html                # Main HTML file for the web UI
│   ├── script.js                 # JavaScript file for front-end interactivity
│   └── styles.css                # CSS file for UI styling
│
├── script.sh                     # Shell script to automate virtual environment setup, install dependencies, and run the app
└── README.md                     # Project documentation file (this file)

```

---

## What This Project Does

1. **Dataset Download & Setup**  
   Downloads the official **Chest X-Ray Pneumonia dataset** from Kaggle and organizes it into training, validation, and testing sets.

2. **Data Augmentation & Preprocessing**  
   Uses `ImageDataGenerator` to apply transformations like zoom, rotation, flipping, etc., to increase data diversity and improve model generalization.

3. **Model Building with Keras Tuner**  
   Implements a CNN with 3 convolutional layers, dense layers, and dropout. Uses **Keras Tuner** to automatically find the best:
   - Number of filters
   - Dense units
   - Dropout rate
   - Optimizer

4. **Model Training & Evaluation**  
   Trains the CNN using binary classification (Normal vs Pneumonia) and evaluates it on the validation and test sets.

5. **Web Deployment with Flask**  
   Integrates the trained model into a Flask web server, enabling users to:
   - Upload chest X-ray images
   - Automatically resize and preprocess them
   - Predict if the image shows pneumonia or not
   - View results in the browser in real-time

6. **User Interface**  
   A simple HTML form lets users interact with the backend without needing technical knowledge. Upload an image and instantly see the prediction result.

---

---

## Tools & Technologies Used

- **Programming Languages**: Python, HTML, CSS, JavaScript
- **Frameworks**: Flask (Python), TensorFlow (for CNN model)
- **Libraries**: Flask-CORS, Boto3, Pillow
- **Styling**: Tailwind CSS (optional), Bootstrap (or custom CSS for UI design)
- **Database**: None (local storage for images)
- **Version Control**: Git, GitHub
- **Other Tools**: Shell scripting, Cron jobs for automation

---

## Backend

The **Backend** folder contains the following components:

- **requirements.txt**: Specifies the required dependencies (e.g., Flask, TensorFlow, Pillow, etc.) that can be installed via `pip install -r requirements.txt`.
- **cnn_model.py**: Python code that defines the CNN model for pneumonia detection, including training and prediction logic.
- **app.py**: Flask-based server file that serves the web interface, receives image uploads, handles inference requests, and returns results.

### Setting up the Backend

To set up the backend environment, follow these steps:

1. Navigate to the **Backend** directory.
2. Create a virtual environment (if not already created):
   ```
   python3.12 -m venv tf-venv
   source tf-venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## Frontend

The **Frontend** folder contains files responsible for the user interface.

- **app2.py**: This is the Flask file that serves the frontend. It handles routes for rendering the HTML page, accepting file uploads, and providing predictions.
- **index.html**: The main HTML file that defines the structure of the web application. It includes a file upload form, image preview area, and a prediction result area.
- **script.js**: JavaScript file that manages the image upload, file validation, image preview functionality, and submission behavior.
- **styles.css**: Contains styling rules for the web application. You can customize the UI using either this file or use a framework like Bootstrap.

### UI Components

1. **File Upload**: The file upload component allows users to select an image file (PNG, JPG, JPEG). It validates file types both on the client-side (JavaScript) and server-side (Flask).
2. **Image Preview**: Once an image is uploaded, it is displayed as a preview before the user clicks on the "Predict" button.
3. **Prediction Results**: After the model processes the image, the prediction result is displayed on the webpage.

---

## Shell Script (`script.sh`)

The **script.sh** file is responsible for automating several steps for setting up the virtual environment, installing dependencies, and running the application.

- **Virtual Environment Setup**: The script creates a virtual environment, installs dependencies, and runs the Flask app.
- **Cron Job Setup**: The script can also be used to run regular tasks like training the model or updating logs automatically.

To use the script, make sure it is executable by running:
```
chmod +x script.sh
```
You can then execute it with:
```
./script.sh
```

---

## Cron Jobs

The **cron job** is set to execute the `script.sh` at regular intervals (every minute in this case). It is configured via the cron table (`crontab -e`), ensuring that the application stays up-to-date or performs regular maintenance tasks (such as checking for updates or training the model).

Cron job example:
```
* * * * * /bin/bash /home/khushipanchal/Pneumonia_Detection/script.sh >> /home/khushipanchal/cron_log.txt 2>&1
```

---

## Frontend Enhancements

### Bug Fixes & Enhancements

Several bugs were fixed and enhancements were added:

1. **File Upload Validation**: Only image files with extensions `.jpg`, `.jpeg`, or `.png` are allowed. Invalid files will show a user-friendly error message.
2. **Image Preview**: After uploading an image, the app displays a preview of the image before the user clicks on "Predict".
3. **Page Reset Functionality**: After making a prediction, users can clear the form and result with a reset button or by reloading the page. This ensures a fresh start for new submissions.

### JavaScript Enhancements

- **File Type Validation**: Client-side validation to ensure only images are uploaded.
- **Image Preview**: JavaScript function to display the selected image immediately after upload.
- **Reset Button**: A button to clear the input form and results.

---

## Setting up the Project

### 1. Clone the Repository

To get started, clone the project repository to your local machine:

```
git clone https://github.com/khushipanchal0108/Pneumonia_Detection.git
cd Pneumonia_Detection
```

### 2. Set up the Backend

### 3. Set up the Frontend

### 4. Running the Application

1. Start the Flask backend by running `python app2.py` in the `Frontend` directory.
2. The app will be available at `http://127.0.0.1:5000/`.

### 5. Running the Shell Script

Use `./script.sh` to automate the setup and start the Flask app.




