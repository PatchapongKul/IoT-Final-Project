import joblib
import pandas as pd
from flask import Flask, request
from dotenv import load_dotenv
import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS

# Load the trained model
knn_model = joblib.load('knn_model.pkl')
model_columns = joblib.load("knn_model_columns.pkl")

load_dotenv()
# InfluxDB config
BUCKET = os.environ.get('INFLUXDB_BUCKET')
print("connecting to",os.environ.get('INFLUXDB_URL'))
client = InfluxDBClient(url=str(os.environ.get('INFLUXDB_URL')),
token=str(os.environ.get('INFLUXDB_TOKEN')),org=os.environ.get('INFLUXDB_ORG'))
write_api = client.write_api()

app = Flask(__name__)

@app.route('/')
def hello():
    if knn_model:
        return "Model is ready for prediction"
    return "Server is running but something wrongs with the model"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.json
        query = pd.DataFrame([json_data])
        feature_sample = query[model_columns]
        target_sample = query['Room_Occupancy_Count'][0]
        predict_sample = knn_model.predict(feature_sample)
        print("Actual Room Occupancy Count", target_sample,"\tPredicted output:", predict_sample[0])

        point = Point("predict_value")\
        .field("Actual_Occupancy_Count", target_sample)\
        .field("Predicted_Occupancy_Count", predict_sample[0])
        
        write_api.write(BUCKET, os.environ.get('INFLUXDB_ORG'), point)

        return "Model predicted and put in database", 200
    except:
        return "Recheck the data", 400
    
if __name__ == '__main__':
    app.run()