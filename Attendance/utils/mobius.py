import requests
import uuid
from datetime import datetime

# Mobius 서버 URL 및 기본 설정
MOBIUS_URL = "http://www.nsbit2024-ctf.com:7579"
CSE_BASE = "Mobius"
HEADERS = {
    "X-M2M-Origin": "SOrigin",
    "Content-Type": "application/json;ty=4",  # ty=4는 contentInstance를 나타냄
}

def generate_request_id():
    """고유한 X-M2M-RI 생성"""
    return str(uuid.uuid4())

def create_attendance_container():
    """attendance 컨테이너 생성"""
    url = f"{MOBIUS_URL}/{CSE_BASE}"
    headers = {
        "X-M2M-Origin": "SOrigin",
        "Content-Type": "application/json;ty=3",  # ty=3은 container
        "X-M2M-RI": generate_request_id(),
    }
    data = {
        "m2m:cnt": {
            "rn": "attendance"
        }
    }
    # print("[DEBUG] POST 요청 (컨테이너 생성):", url, data)
    response = requests.post(url, json=data, headers=headers)
    # print("[DEBUG] 응답 상태 코드:", response.status_code)
    # print("[DEBUG] 응답 데이터:", response.text)
    if response.status_code in [200, 201]:
        print("[INFO] 'attendance' 컨테이너 생성 성공.")
    else:
        print("[ERROR] 'attendance' 컨테이너 생성 실패:", response.status_code, response.text)

def add_attendance():
    """학번과 시간을 Mobius 서버에 저장"""
    student_id = "20011707"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attendance_data = f"{current_time}, 학번: {student_id}"

    url = f"{MOBIUS_URL}/{CSE_BASE}/attendance"
    headers = HEADERS.copy()
    headers["X-M2M-RI"] = generate_request_id()
    data = {
        "m2m:cin": {
            "cnf": "text/plain:0",
            "con": attendance_data
        }
    }
    # print("[DEBUG] POST 요청 (출석 데이터):", url, data)
    response = requests.post(url, json=data, headers=headers)
    # print("[DEBUG] 응답 상태 코드:", response.status_code)
    # print("[DEBUG] 응답 데이터:", response.text)

    if response.status_code in [200, 201]:
        print(f"[INFO] 출석 기록 저장 성공: {attendance_data}")
    else:
        print("[ERROR] 출석 기록 저장 실패:", response.status_code, response.text)

def get_attendance():
    """출석 정보를 Mobius 서버에서 가져오기"""
    url = f"{MOBIUS_URL}/{CSE_BASE}/attendance/latest"
    headers = {
        "X-M2M-Origin": "SOrigin",
        "X-M2M-RI": generate_request_id(),
        "Accept": "application/json",
    }
    # print("[DEBUG] GET 요청 (최신 출석 데이터 조회):", url)
    response = requests.get(url, headers=headers)
    # print("[DEBUG] 응답 상태 코드:", response.status_code)
    # print("[DEBUG] 응답 데이터:", response.text)

    if response.status_code == 200:
        print("[INFO] 출석 기록 가져오기 성공.")
        data = response.json()
        if "m2m:cin" in data:
            print("[INFO] 저장된 출석 데이터:", data["m2m:cin"]["con"])
        else:
            print("[INFO] 출석 데이터가 없습니다.")
    else:
        print("[ERROR] 출석 기록 가져오기 실패:", response.status_code, response.text)