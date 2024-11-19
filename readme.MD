# MQTT Reservoir Data Publisher and Subscriber

## Overview

This project consists of two main components: an MQTT publisher and an MQTT subscriber. The publisher reads data from CSV files, converts it to JSON, and publishes it to specific MQTT topics. The subscriber listens to these topics, collects the data, and generates daily summary reports in JSON format.

## Project Structure

```
.
├── mqtt_publisher.py
├── mqtt_subscriber.py
├── daily_reports/
│   └── report_2024-11-18.json
├── Oroville_WML(Sample),.csv
├── Shasta_WML(Sample),.csv
└── Sonoma_WML(Sample),.csv
```

## Requirements

- Python 3.x
- `paho-mqtt` library
- `pandas` library

You can install the required libraries using pip:

```sh
pip install paho-mqtt pandas
```

## Usage

### MQTT Publisher

The publisher reads data from the CSV files and publishes it to the MQTT broker.

1. **CSV Files**: Ensure the CSV files (`Oroville_WML(Sample),.csv`, `Shasta_WML(Sample),.csv`, `Sonoma_WML(Sample),.csv`) are present in the project directory.
2. **Run the Publisher**: Execute the `mqtt_publisher.py` script to start publishing data.

```sh
python mqtt_publisher.py
```

### MQTT Subscriber

The subscriber listens to the MQTT topics and generates daily summary reports.

1. **Run the Subscriber**: Execute the `mqtt_subscriber.py` script to start listening for messages.

```sh
python mqtt_subscriber.py
```

2. **Daily Reports**: The subscriber will generate and save daily summary reports in the `daily_reports` directory.

## Configuration

- **MQTT Broker**: The broker is set to `localhost` and the port to `1883`. You can change these settings in both `mqtt_publisher.py` and `mqtt_subscriber.py` if needed.

## Files

- `mqtt_publisher.py`: Publishes data from CSV files to MQTT topics.
- `mqtt_subscriber.py`: Subscribes to MQTT topics and generates daily summary reports.
- `daily_reports/`: Directory where daily summary reports are saved.
- `Oroville_WML(Sample),.csv`, `Shasta_WML(Sample),.csv`, `Sonoma_WML(Sample),.csv`: Sample CSV files containing reservoir data.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.