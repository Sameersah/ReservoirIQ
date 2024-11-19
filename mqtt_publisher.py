import paho.mqtt.client as mqtt
import pandas as pd
import json
import time

# File paths for the CSV files
oroville_csv = "Oroville_WML(Sample),.csv"
shasta_csv = "Shasta_WML(Sample),.csv"
sonoma_csv = "Sonoma_WML(Sample),.csv"

# MQTT broker details
broker = "localhost"
port = 1883

# Initialize MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port)

# Function to load CSV data and convert to JSON
def load_csv_to_json(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")
        return []

# Function to publish data
def publish_data(topic, data):
    for entry in data:
        message = json.dumps(entry)
        client.publish(topic, message)
        print(f"Published to {topic}: {message}")
        time.sleep(1)  # Simulate a delay

# Load data from CSV files
oroville_data = load_csv_to_json(oroville_csv)
shasta_data = load_csv_to_json(shasta_csv)
sonoma_data = load_csv_to_json(sonoma_csv)

# Publish data to respective topics
publish_data("OROVILLE/WML", oroville_data)
publish_data("SHASTA/WML", shasta_data)
publish_data("SONOMA/WML", sonoma_data)

# Disconnect client
client.disconnect()
