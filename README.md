# Pneumonia Detection from Chest X-Ray Images using Deep Learning

This project is a complete pipeline for **detecting pneumonia from chest X-ray images** using **Convolutional Neural Networks (CNNs)** with automated **hyperparameter tuning** via **Keras Tuner**, and a **Flask web application** to allow real-time predictions from user-uploaded images.

The core objective is to build a medical image classifier that distinguishes between **normal** lungs and those affected by **pneumonia**, enabling faster preliminary screening which can assist healthcare professionals.

This project demonstrates not only **deep learning model building and optimization**, but also how to **deploy the model** into a usable web service for real-world interaction.

---

## Project Structure

```
pneumonia-detection/
├── app2.py                           # Flask backend API to serve predictions
├── best_pneumonia_cnn_model.h5      # Final trained CNN model file
├── chest_xray/                      # Dataset directory containing train/val/test folders
│   ├── train/
│   ├── val/
│   └── test/
├── templates/
│   └── index.html                   # HTML frontend for uploading images
├── requirements.txt                 # List of Python dependencies
├── kaggle.json                      # Kaggle API credentials (user-provided)
└── README.md                        # Project documentation
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

This project showcases the end-to-end machine learning lifecycle:
- From data acquisition,
- To model design and optimization,
- To deployment in a real-world user interface.

Ideal for academic projects, beginner ML portfolios, or as a foundation for building medical AI applications.
