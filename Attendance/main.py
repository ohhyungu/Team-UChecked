from utils.mobius import create_attendance_container, add_attendance, get_attendance


def main():
    print("=== 출석 체크 시스템 ===")

    # 컨테이너 생성
    #print("[INFO] Mobius 서버에 'attendance' 컨테이너 생성 시도...")
    #create_attendance_container()

    # 출석 데이터 저장
    print("[INFO] Mobius 서버에 출석 데이터 저장 시도...")
    add_attendance()

    # 저장된 출석 데이터 조회
    print("[INFO] Mobius 서버에서 출석 데이터 조회 시도...")
    get_attendance()


if __name__ == "__main__":
    main()