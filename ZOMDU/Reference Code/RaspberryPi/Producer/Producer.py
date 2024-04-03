"""
MQTT Smart temperature Sensor
"""
#Importing relevant modules
import pandas as pd
import numpy as np
import time
import paho.mqtt.client as mqtt
import json

# let's connect to the MQTT broker
MQTT_BROKER_URL    = "202.28.193.101"
MQTT_PUBLISH_TOPIC = "@msg/data"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)
df = pd.read_csv('test_cases.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    payload = row.to_dict()
    mqttc.publish(MQTT_PUBLISH_TOPIC, json.dumps(payload))
    print(f"Published new measurement: {json.dumps(payload)}")
    time.sleep(5)