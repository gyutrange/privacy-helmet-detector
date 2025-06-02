import cv2
from helmet_detector import HelmetDetector
from face_masker import FaceMasker

cap = cv2.VideoCapture(0)  # 또는 산업용 CCTV 스트림 URL

helmet_detector = HelmetDetector(model_path='best.pt')  # 학습된 커스텀 모델 사용
face_masker = FaceMasker()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = face_masker.apply_blur(frame)
    frame = helmet_detector.detect_helmet(frame)

    cv2.imshow("Industrial AI Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
