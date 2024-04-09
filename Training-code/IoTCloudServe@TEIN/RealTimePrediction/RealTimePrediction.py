"""
Real-Time prediction
Retrieve streaming data from the consumer and predict the number 
of people inside the room. Utilize Flask, a simple REST API server, 
as the endpoint for data feeding.
"""

# Importing relevant modules
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS
import json

# Load the trained model
knn_model = joblib.load('knn_model.pkl')
model_columns = joblib.load("knn_model_columns.pkl")

# Load environment variables from ".env"
load_dotenv()

# InfluxDB config
BUCKET = os.environ.get('INFLUXDB_BUCKET')
print("connecting to",os.environ.get('INFLUXDB_URL'))
client = InfluxDBClient(
    url=str(os.environ.get('INFLUXDB_URL')),
    token=str(os.environ.get('INFLUXDB_TOKEN')),
    org=os.environ.get('INFLUXDB_ORG')
)
write_api = client.write_api()

# Create simple REST API server
app = Flask(__name__)

# Default route: check if model is available.
@app.route('/')
def check_model():
    if knn_model:
        return "Model is ready for prediction"
    return "Server is running but something wrongs with the model"

# Predict route: predict the output from streaming data
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON text from the request
        json_text = request.data
        # Convert JSON text to JSON object
        json_data = json.loads(json_text)
        # Add to dataframe
        query = pd.DataFrame([json_data])
        # Extract features and label from data
        feature_sample = query[model_columns]
        target_sample = query['Room_Occupancy_Count'][0]
        # Predict the number of people inside the room
        predict_sample = knn_model.predict(feature_sample)
        print("Actual Room Occupancy Count", int(target_sample),"\tPredicted output:", int(predict_sample[0]))
        # Assign the true label and predicted label into Point
        point = Point("predict_value")\
            .field("Actual_Occupancy_Count", target_sample)\
            .field("Predicted_Occupancy_Count", predict_sample[0])
        
        # Write that Point into database
        write_api.write(BUCKET, os.environ.get('INFLUXDB_ORG'), point)
        return jsonify({"Actual Room Occupancy Count": int(target_sample), "Predicted output": int(predict_sample[0])}), 200
    
    except:
        # Something error with data or model
        return "Recheck the data", 400
    
if __name__ == '__main__':
    app.run()