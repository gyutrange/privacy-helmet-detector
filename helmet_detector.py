import torch
import cv2
import numpy as np

class HelmetDetector:
    def __init__(self, model_path='yolov5s.pt'):  # 커스텀 모델 사용 시 경로 변경
        self.model = torch.hub.load('yolov5', 'custom', path=model_path, source='local')  # 로컬 YOLOv5 사용
        self.model.conf = 0.4

    def detect_helmet(self, frame):
        results = self.model(frame)
        labels, coords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        h, w, _ = frame.shape

        for label, cord in zip(labels, coords):
            x1, y1, x2, y2, conf = int(cord[0]*w), int(cord[1]*h), int(cord[2]*w), int(cord[3]*h), cord[4]
            class_name = self.model.names[int(label)]
            color = (0, 255, 0) if "helmet" in class_name.lower() else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        return frame
