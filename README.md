
# Pneumonia Detection from Chest X-Ray Images using Deep Learning (Linux-Based)

This project focuses on detecting **pneumonia from chest X-ray images** using a **deep learning model built with CNNs**, hosted in a **Flask web application**, and deployed and automated on a **Linux environment**.

As part of our Open Source Technology coursework, we developed this complete pipeline, starting from dataset preprocessing, model training with **automated hyperparameter tuning**, local Flask deployment for real-time inference, resolving issues collaboratively, and automating the process via **shell scripting** and **cron jobs**. The project demonstrates the practical use of Linux, Python, and open-source tools to build a medical-grade AI solution from scratch.

---

## Project Structure

```
Pneumonia_Detection/
│
├── Backend/
│   ├── cnn_model.py              # CNN model training and hyperparameter tuning
│   ├── requirements.txt          # Python dependencies for training and inference
│
├── Frontend/
│   ├── app2.py                   # Flask app handling image upload and prediction
│   ├── index.html                # Frontend UI for users
│   ├── script.js                 # JavaScript for frontend validation and preview
│   ├── styles.css                # Custom styles for frontend
│
├── script.sh                     # Shell script to automate environment setup and app execution
├── cron_log.txt                  # Output log file for cron job (auto-generated)
└── README.md                     # Project documentation
```

---

## Key Features

### 1. Model Training and Hyperparameter Tuning

- Utilizes **TensorFlow/Keras** to define a CNN with convolutional and dense layers.
- Incorporates **Keras Tuner** to search for optimal hyperparameters:
  - Number of filters
  - Dense units
  - Dropout rates
  - Optimizer choice
- Employs **data augmentation** (`ImageDataGenerator`) for generalization.
- Separates dataset into training, validation, and testing sets.

### 2. Flask-Based Prediction System

- **Flask server** to handle:
  - Image upload via HTML form
  - Resizing and preprocessing uploaded images
  - Model inference
  - Returning prediction result to the user
- Accessible locally via `http://127.0.0.1:5000`

### 3. Linux-Based Shell Scripting & Automation

- **script.sh** automates:
  - Creating a Python virtual environment
  - Installing dependencies
  - Launching the Flask application
- **Cron job** executes this script at scheduled intervals, enabling continuous automation.

### 4. Bug Resolution via Open Source Workflow

- Raised issues on GitHub during development (e.g., file validation, error handling).
- Collaboratively debugged and resolved using Linux command-line tools and Git.
- Ensured version control through meaningful commits and branch management.

---

## Technology Stack

- **Languages**: Python, HTML, CSS, JavaScript
- **Frameworks**: TensorFlow, Keras, Flask
- **Frontend**: Plain HTML/CSS, optional Tailwind
- **Utilities**: Shell scripting, Cron jobs
- **Version Control**: Git, GitHub

---

## Backend Details

Located in the `Backend/` folder.

- `cnn_model.py`: Trains the CNN and saves the model.
- `requirements.txt`: Python dependencies (`tensorflow`, `flask`, `keras-tuner`, `pillow`, etc.)

---

## Frontend Details

Located in the `Frontend/` folder.

- `app2.py`: Flask app for rendering HTML and serving predictions.
- `index.html`: Upload interface with form and prediction output.
- `script.js`: Enhances frontend with:
  - File format validation
  - Image preview
  - Reset functionality
- `styles.css`: Basic styling for layout and responsiveness.

---

## Shell Script (`script.sh`)

Automates the entire setup and execution pipeline.

- Creates a virtual environment
- Installs dependencies
- Activates the environment
- Starts the Flask server
- Logs execution if called via `cron`

Make executable:
```bash
chmod +x script.sh
```

Run manually:
```bash
./script.sh
```

---

## Cron Job Integration

To automate execution:

```bash
crontab -e
```

Add the following line to run `script.sh` every minute:

```
* * * * * /bin/bash /home/khushipanchal/Pneumonia_Detection/script.sh >> /home/khushipanchal/cron_log.txt 2>&1
```

This ensures the application restarts automatically or performs periodic tasks like model retraining or logging.

---

## User Interface Features

- **File Upload**: Accepts `.jpg`, `.jpeg`, `.png` files.
- **Live Preview**: Displays image preview post-upload.
- **Prediction Display**: Results shown in real-time upon submission.
- **Reset Functionality**: Clears UI without refreshing the page.

---

## Deployment Workflow (Linux)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/khushipanchal0108/Pneumonia_Detection.git
   cd Pneumonia_Detection
   ```

2. **Run Shell Script**:
   ```bash
   ./script.sh
   ```

3. **Access Web App**:
   Open `http://127.0.0.1:5000/` in your browser.

4. **Enable Cron Job**:
   Use `crontab -e` to schedule automation.

