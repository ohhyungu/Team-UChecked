# simulate_attendance.py

import requests
import uuid
import json
from datetime import datetime
import time

# Mobius 서버 설정
mobius_url = "http://www.nsbit2024-ctf.com:7579/Mobius"

# 출석 데이터 생성 함수
def send_attendance(student_id):
    # 비콘 감지 시뮬레이션을 위한 가상 데이터
    student_name = "학생1"  # 고정된 이름, 필요에 따라 변경 가능
    course_id = "Course102"
    course_name = "시스템해킹과보안"
    beacon_id = "Beacon001"
    attendance_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    attendance_status = "출석"  # 출석, 지각, 결석 등으로 변경 가능

    # Content Instance 생성
    headers = {
        "X-M2M-Origin": "S20011707",  # Origin을 S + 학번으로 설정
        "X-M2M-RI": str(uuid.uuid4()),
        "Content-Type": "application/json; ty=4",  # Content Instance 타입
        "Accept": "application/json"
    }

    content = {
        "student_id": student_id,
        "student_name": student_name,
        "course_id": course_id,
        "course_name": course_name,
        "beacon_id": beacon_id,
        "attendance_time": attendance_time,
        "attendance_status": attendance_status
    }

    payload = {
        "m2m:cin": {
            "con": json.dumps(content, ensure_ascii=False),
            "lbl": [student_id]  # lbl 필드 설정
        }
    }

    attendance_url = f"{mobius_url}/Attendance"

    response = requests.post(attendance_url, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        print(f"[SUCCESS] 출석 데이터 전송 성공: {attendance_time}")
    else:
        print(f"[FAIL] 출석 데이터 전송 실패: {response.text}")

def main():
    print("출석 체크 시뮬레이션 프로그램")
    print("학번을 입력하면 출석 체크가 시뮬레이션됩니다.")
    print("종료하려면 'exit'를 입력하세요.\n")

    while True:
        student_id = input("학번을 입력하세요 (예: 20011707): ").strip()
        if student_id.lower() == 'exit':
            print("시뮬레이션을 종료합니다.")
            break
        if student_id != "20011707":
            print("잘못된 학번입니다. 다시 입력하세요.\n")
            continue
        send_attendance(student_id)
        print()

if __name__ == "__main__":
    main()