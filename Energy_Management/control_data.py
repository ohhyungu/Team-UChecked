import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
MOBIUS_URL = os.getenv("MOBIUS_URL", "http://localhost:7579/Mobius")

def seasonal_control(temperature):
    month = datetime.now().month
    if month in [6, 7, 8]:
        return "TURN_ON_COOLING" if temperature > 25 else "TURN_OFF_COOLING"
    elif month in [12, 1, 2]:
        return "TURN_ON_HEATING" if temperature < 20 else "TURN_OFF_HEATING"
    return "IDLE"

def get_sensor_data(sensor_type):
    url = f"{MOBIUS_URL}/SensorAE/{sensor_type}/la"
    headers = {
        "X-M2M-Origin": "admin:admin",
        "X-M2M-RI": "requestID",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["m2m:cin"]["con"]
        if sensor_type == "presence":
            return data.lower() == "true"  # Convert to boolean
        return float(data)
    else:
        print(f"Failed to fetch data for {sensor_type}, status code: {response.status_code}")
        return None

def send_control_command(command):
    url = f"{MOBIUS_URL}/ControlAE/commands"
    headers = {
        "X-M2M-Origin": "admin:admin",
        "X-M2M-RI": "requestID789",
        "Content-Type": "application/json;ty=4",
    }
    payload = {
        "m2m:cin": {
            "con": command
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"Command Sent: {command}, Response: {response.status_code}")
    else:
        print(f"Failed to send command. Status code: {response.status_code}, Response: {response.text}")

def analyze_and_send_command():
    temperature = get_sensor_data("temperature")
    presence = get_sensor_data("presence")
    
    if temperature is not None and presence is not None:
        if presence:
            command = seasonal_control(temperature)
        else:
            command = "TURN_OFF_ALL"
        send_control_command(command)
    else:
        print("Could not fetch sensor data.")

while True:
    analyze_and_send_command()
    time.sleep(10)

