import cv2
from ultralytics import YOLO
import torch

model_path = './last_68epochs_8n.pt'
model = YOLO(model_path).to(torch.device(0))

cap = cv2.VideoCapture(0)

while cap.isOpened():

    success, frame = cap.read()

    if success:

        results = model.track(source=frame, persist=True, iou=0.6, conf=0.4)

        annotated_frame = results[0].plot()

        cv2.imshow("Custom Model Output", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    
    else:
        break
cap.release()
cv2.destroyAllWindows()