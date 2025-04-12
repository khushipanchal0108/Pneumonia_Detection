// Preview uploaded image and validate
function previewImage() {
    const fileInput = document.getElementById('image-upload');
    const file = fileInput.files[0];
    const preview = document.getElementById('uploaded-image');

    if (file) {
        if (!validateFileType(file)) {
            preview.style.display = 'none';
            return;
        }

        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

// Validate file type
function validateFileType(file) {
    const validTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    if (!validTypes.includes(file.type)) {
        alert("Error: Please upload only .jpg, .jpeg, or .png files.");
        return false;
    }
    return true;
}

// Submit image for prediction
function submitImage() {
    const fileInput = document.getElementById('image-upload');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image first.");
        return;
    }

    if (!validateFileType(file)) {
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('prediction-result');
        if (data.prediction) {
            resultElement.textContent = `Prediction: ${data.prediction}`;
        } else {
            resultElement.textContent = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('prediction-result').textContent = "Error predicting image.";
    });
}

// Clear/reset form
function resetForm() {
    const fileInput = document.getElementById('image-upload');
    const preview = document.getElementById('uploaded-image');
    const result = document.getElementById('prediction-result');

    fileInput.value = '';
    preview.src = '';
    preview.style.display = 'none';
    result.textContent = 'Prediction Result will appear here';
}
