# Brain Tumor Classification

This project provides a web application for classifying brain MRI images to detect the presence of tumors using machine learning.

![Project Screenshot](screenshot.png)

## Important Note

Due to file size limitations on GitHub, the `brain_tumor_model.keras` file is not included in this repository. You will need to either train the model yourself using the provided notebook or download the pre-trained model separately.

## Getting Started

Install Using Docker

If you prefer to use the pre-trained model without going through the training process, you can use Docker:

1. Pull the Docker image:
   ```
   docker pull pouryare/brain-tumor-classification:latest
   ```

2. Run the Docker container:
   ```
   docker run -p 8080:8080 pouryare/brain-tumor-classification:latest
   ```

3. Open a web browser and navigate to `http://localhost:8080`

## Usage

Once the application is running:

1. You'll see an interface to upload a brain MRI image (JPG format only).
2. Click on "Choose File" to select an MRI image from your computer.
3. Click "Upload and Analyze" to process the image.
4. The application will display the prediction result: No Brain Tumor or Brain Tumor Detected, along with a confidence score.

## Project Structure

- `app.py`: Main Flask application containing both the web server and model logic
- `requirements.txt`: List of Python dependencies
- `Dockerfile`: Instructions for building the Docker image
- `templates/index.html`: HTML template for the web interface
- `Brain_Tumor_Classification.ipynb`: Jupyter notebook for model training
- `brain_tumor_model.keras`: Trained model file (not included in the repository)
- `static/uploads/`: Directory for temporarily storing uploaded images

## Acknowledgements

Special thanks to Preet Viradiya for providing the dataset on Kaggle.
