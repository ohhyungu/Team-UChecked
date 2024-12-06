import cv2
import torch
import numpy as np

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 관심 영역 정의 (네모모양 영역)
rectangles = [(100, 100, 800, 500), (900, 100, 1600, 500), (100, 600, 800, 1000), (900, 600, 1600, 1000)]

while True:
    # 프레임 읽어오기
    ret, frame = cap.read()

    # 관심 영역에 빨간색 사각형 그리기
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # 각 관심 영역별로 사람 수와 객체 존재 여부 추적
    num_persons_list = []   # 각 관심 영역별 사람 수 저장
    object_present_list = []  # 각 관심 영역별 객체 존재 여부 저장

    for i, rect in enumerate(rectangles):
        x1, y1, x2, y2 = rect
        roi = frame[y1:y2, x1:x2]  # 관심 영역 추출
        results = model(roi)  # YOLOv5 모델로 객체 검출 수행

        # 관심 영역에서 사람 수 계산
        num_persons = len(results.pred[0][results.pred[0][:, 5] == 0])
        num_persons_list.append(num_persons)

        # 관심 영역에 노트북, 컵, 책, 가방, 핸드백이 있는지 여부 판단
        object_present = any([
            results.pred[0][results.pred[0][:, 5] == 63].any(),  # 노트북
            results.pred[0][results.pred[0][:, 5] == 41].any(),  # 컵
            results.pred[0][results.pred[0][:, 5] == 73].any(),  # 책
            results.pred[0][results.pred[0][:, 5] == 24].any(),  # 가방
            results.pred[0][results.pred[0][:, 5] == 26].any()   # 핸드백
        ])
        object_present_list.append(object_present)

        # 검출된 객체에 초록색 바운딩 박스 그리기
        for result in results.pred[0]:
            label = int(result[5])
            if label in [0, 63, 41, 73, 24, 26]:
                x1, y1, x2, y2 = result[:4].int().cpu().numpy()
                cv2.rectangle(roi, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 화면에 관심 영역별로 사람 수와 객체 존재 여부 표시
    for i, rect in enumerate(rectangles):
        x1, y1, _, _ = rect
        cv2.putText(frame, f"Area {i + 1}'s people: {num_persons_list[i]}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, f"Area {i + 1}'s objects: {'Yes' if object_present_list[i] else 'No'}", (x1, y1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 결과를 화면에 표시
    cv2.imshow('YOLOv5 Space Congestion Analysis', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
