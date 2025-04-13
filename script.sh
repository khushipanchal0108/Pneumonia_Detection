#!/bin/bash 
echo "Starting Pneumonia Detection App..." 

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "tf-venv" ]; then 
    echo "Creating virtual environment..."
    python3 -m venv tf-venv 
fi

# Step 2: Activate virtual environment
echo "Activating virtual environment..."
source tf-venv/bin/activate

# Step 3: Install backend requirements
echo "Installing backend requirements..."
cd Backend
pip install -r requirements.txt
cd ..

# Step 4: Run Flask app
echo "Launching Flask App..."
cd Frontend
python app2.py

