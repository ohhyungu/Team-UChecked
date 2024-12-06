import requests
import time

def fetch_latest_command():
    """
    Mobius 플랫폼에서 가장 최근의 명령을 가져옵니다.
    """
    url = "http://localhost:7579/Mobius/ControlAE/commands/la"
    headers = {
        "X-M2M-Origin": "admin:admin",
        "X-M2M-RI": "requestID123"
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        if response.status_code == 200:
            return response.json()["m2m:cin"]["con"]
        else:
            print("Failed to fetch the latest command.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the latest command: {e}")
        return None

def execute_command(command):
    """
    가져온 명령에 따라 장치를 제어합니다.
    """
    print(f"Executing command: {command}")
    # 실제 장치 제어 로직을 여기에 작성
    if command == "TURN_OFF_ALL":
        print("Turning off all devices.")
    elif command == "TURN_ON_ALL":
        print("Turning on all devices.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    while True:
        latest_command = fetch_latest_command()
        if latest_command:
            execute_command(latest_command)
        time.sleep(5)

