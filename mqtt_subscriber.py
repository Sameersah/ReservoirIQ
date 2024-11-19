import paho.mqtt.client as mqtt
import json
import os
from datetime import datetime

# MQTT broker details
broker = "localhost"
port = 1883

# Data store to collect messages
data_store = {"OROVILLE/WML": [], "SHASTA/WML": [], "SONOMA/WML": []}

# Callback function when a message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        data_store[topic].append(data)
        print(f"\nReceived from {topic}: {data}")
        generate_daily_report()  # Generate and save report on each new message
    except json.JSONDecodeError:
        print(f"Failed to decode message from {topic}: {payload}")

# Function to generate and save daily summary report
def generate_daily_report():
    print("\n--- Daily Summary Report ---")
    report = []
    for topic, messages in data_store.items():
        if messages:
            reservoir = topic.split('/')[0]
            total_taf = sum(msg['TAF'] for msg in messages)
            entries_count = len(messages)
            reservoir_report = {
                "Reservoir": reservoir,
                "Total_TAF": total_taf,
                "Entries_Received": entries_count,
                "Date": datetime.now().strftime("%Y-%m-%d")
            }
            report.append(reservoir_report)
            print(f"Reservoir: {reservoir}")
            print(f"  Total TAF: {total_taf}")
            print(f"  Entries Received: {entries_count}")

    print("----------------------------")
    save_report_to_file(report)

# Function to save report to a JSON file
def save_report_to_file(report):
    output_dir = "daily_reports"
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{output_dir}/report_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(file_name, "w") as f:
        json.dump(report, f, indent=4)
    print(f"Report saved to {file_name}")

# Initialize MQTT client
client = mqtt.Client()

# Set the callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to topics
client.subscribe("OROVILLE/WML")
client.subscribe("SHASTA/WML")
client.subscribe("SONOMA/WML")

# Start listening for messages indefinitely
print("Subscriber is listening... Press Ctrl+C to stop.")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nStopping subscriber...")

# Disconnect the client (executes when you manually stop the script)
client.disconnect()
