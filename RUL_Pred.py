from flask import Flask, request, jsonify
import pandas as pd
import pickle  # Use pickle to load your pre-trained model
from sklearn.preprocessing import StandardScaler
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

# Load your pre-trained model using pickle
try:
    with open('RUL_model.pkl', 'rb') as model_file:
        regressor = pickle.load(model_file)
    logging.info("Regression model loaded successfully")
except Exception as e:
    logging.error(f"Error loading the regression model: {str(e)}")
    raise

# Load your pre-trained scaler using pickle
try:
    with open('RUL_model_scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    logging.info("Scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading the scaler: {str(e)}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Log the input JSON data
        logging.info(f"Input JSON data: {data}")
        
        # Convert the JSON data into a DataFrame
        input_data = pd.DataFrame(data, index=[0])
        
        # Log the input data after conversion
        logging.info(f"Input data (DataFrame):\n{input_data}")
        
        # Scale the input data using the loaded scaler
        scaled_input_data = scaler.transform(input_data)
        
        # Log the scaled input data
        logging.info(f"Scaled input data:\n{scaled_input_data}")
        
        # Make predictions using the loaded regression model
        prediction = regressor.predict(scaled_input_data)
        
        # Log the prediction
        logging.info(f"Prediction: {prediction[0]}")
        
        # Return the prediction as JSON response
        response = {'prediction': prediction[0]}
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
