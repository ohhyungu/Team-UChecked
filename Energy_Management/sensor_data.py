import requests
import random
import time
from db_config import get_db_connection
from dotenv import load_dotenv
import os

load_dotenv()
MOBIUS_URL = os.getenv("MOBIUS_URL")

def send_sensor_data(sensor_type, data):
    url = f"{MOBIUS_URL}/SensorAE/{sensor_type}"
    headers = {
        "X-M2M-Origin": "admin:admin",
        "X-M2M-RI": "requestID123",  # 요청 ID 추가
        "Content-Type": "application/json;ty=4"
    }
    payload = {
        "m2m:cin": {
            "con": data
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"Sent {sensor_type}: {data}, Response: {response.status_code}")

    # MySQL에 데이터 저장
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO sensor_data (sensor_type, value) VALUES (%s, %s)"
            cursor.execute(sql, (sensor_type, data))
        connection.commit()
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        connection.close()

while True:
    temperature = round(random.uniform(18.0, 30.0), 1)
    presence = random.choice(["true", "false"])
    send_sensor_data("temperature", str(temperature))
    send_sensor_data("presence", presence)
    time.sleep(5)

