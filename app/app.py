from flask import Flask, render_template, request, jsonify
import numpy as np
import os
from tensorflow import keras
from PIL import Image, ImageOps

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
model = keras.models.load_model(os.path.join(os.getcwd(), 'brain_tumor_model.keras'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = ImageOps.grayscale(img)
    img = img.resize((150, 150))
    img_array = np.array(img)
    img_array = img_array.reshape((1, 150, 150, 1)) / 255.0
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
        file.save(filename)
        
        preprocessed_image = preprocess_image(filename)
        prediction = model.predict(preprocessed_image)
        
        result = 'No Brain Tumor' if prediction[0][0] > 0.5 else 'Brain Tumor Detected'
        confidence = float(prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0])
        
        return jsonify({
            'result': result,
            'confidence': f'{confidence:.2%}',
            'image_path': '/static/uploads/uploaded_image.jpg'
        })
    
    return jsonify({'error': 'File type not allowed. Please upload a JPG image.'})

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=8080)