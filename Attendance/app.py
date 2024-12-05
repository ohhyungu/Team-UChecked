# app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO
import requests
import uuid
import json
from urllib.parse import urljoin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # 실제 환경에서는 안전한 비밀 키로 변경하세요.
socketio = SocketIO(app)

# Mobius 서버 설정
mobius_base_url = "http://www.nsbit2024-ctf.com:7579"
csebase_path = "/Mobius/"
mobius_url = urljoin(mobius_base_url, csebase_path)  # 최종 URL: http://www.nsbit2024-ctf.com:7579/Mobius/

# Mobius 서버에 Subscription 생성
def create_subscription():
    subscription_url = urljoin(mobius_url, "Attendance")
    headers = {
        'X-M2M-Origin': 'SOrigin',
        'X-M2M-RI': str(uuid.uuid4()),
        'Content-Type': 'application/json; ty=23',  # Subscription resource type is 23
        'Accept': 'application/json'
    }
    # 알림을 받을 Flask 앱의 /notify 엔드포인트 URL
    notify_url = "http://www.nsbit2024-ctf.com:5000/notify"  # 실제 Flask 앱의 URL로 변경하세요.

    payload = {
        "m2m:sub": {
            "rn": "AttendanceSubscription",
            "nu": [notify_url],  # 배열로 변경
            "enc": {
                "net": [3]  # Notification for CREATE operations
            }
        }
    }

    response = requests.post(subscription_url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        print("[INFO] Subscription 생성 성공")
    elif response.status_code == 409:
        print("[INFO] 이미 Subscription이 존재합니다.")
    else:
        print(f"[ERROR] Subscription 생성 실패: {response.text}")

# 애플리케이션 시작 시 Subscription 생성
create_subscription()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notify', methods=['POST'])
def notify():
    notification = request.get_json()
    print("알림 수신:", notification)

    # 출석 데이터 파싱
    cin = notification.get('m2m:cin', {})
    con = cin.get('con', '')
    if con:
        try:
            # 'con' 필드가 JSON 문자열일 경우 파싱
            if isinstance(con, str):
                attendance_info = json.loads(con)
            else:
                attendance_info = con
        except json.JSONDecodeError as e:
            print(f"[ERROR] 출석 데이터 JSON 파싱 오류: {e}")
            return '', 400

        # 출석 데이터 구조에 맞게 필드 추출
        student_id = attendance_info.get('student_id')
        student_name = attendance_info.get('student_name')
        course_id = attendance_info.get('course_id')
        course_name = attendance_info.get('course_name')
        attendance_time = attendance_info.get('attendance_time')
        attendance_status = attendance_info.get('attendance_status')

        if student_id and student_name and course_id and course_name and attendance_time and attendance_status:
            attendance_data = {
                'student_id': student_id,
                'student_name': student_name,
                'course_id': course_id,
                'course_name': course_name,
                'attendance_time': attendance_time,
                'attendance_status': attendance_status
            }
            # 클라이언트로 실시간 알림 전송
            socketio.emit('new_attendance', attendance_data, broadcast=True)
            print(f"[INFO] 새로운 출석 데이터: {attendance_data}")
        else:
            print("[WARNING] 출석 데이터 필드 누락")
    return '', 200

@socketio.on('connect')
def handle_connect():
    print("클라이언트가 연결되었습니다.")

@socketio.on('disconnect')
def handle_disconnect():
    print("클라이언트가 연결을 끊었습니다.")

if __name__ == '__main__':
    # Flask 앱이 외부에서 접근 가능하도록 호스트를 '0.0.0.0'으로 설정
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)