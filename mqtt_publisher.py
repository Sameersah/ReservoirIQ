import paho.mqtt.client as mqtt
import json
import time

# Data to be published
oroville_data = [{"Date": "9/29/2024", "TAF": 2000}, {"Date": "9/30/2024", "TAF": 2001}]
shasta_data = [{"Date": "9/29/2024", "TAF": 2720}, {"Date": "9/30/2024", "TAF": 2727}]
sonoma_data = [{"Date": "9/29/2024", "TAF": 192}, {"Date": "9/30/2024", "TAF": 193}]

# MQTT broker details
broker = "localhost"
port = 1883

# Initialize MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port)

# Function to publish data
def publish_data(topic, data):
    for entry in data:
        message = json.dumps(entry)
        client.publish(topic, message)
        print(f"Published to {topic}: {message}")
        time.sleep(1)  # Simulate a delay

# Publish data to respective topics
publish_data("OROVILLE/WML", oroville_data)
publish_data("SHASTA/WML", shasta_data)
publish_data("SONOMA/WML", sonoma_data)

# Disconnect client
client.disconnect()
