import cv2
from ultralytics import YOLO
import torch

model = YOLO('./test_deep-sort-realtime/last_261epochs_8n.pt').to(torch.device(0))

cap = cv2.VideoCapture(0)
m_status = 1
edge_status = 0

def movementStatus(track_xyxy, num_stb, edge_status):
    if edge_status == 1:
        if num_stb > 1:
            m_status = 0
            print("If cond (num_stb > 1) in movement status")
        elif num_stb == 1:
            m_status = 1
            print("Elif cond (num_stb == 1) in movement status")
        else:
            m_status = 1
            print("Else cond in movement status")
    elif edge_status == 0:
        m_status = 1
        print("Elif in movement status")
    print("Movement status : " + str(m_status))
    cv2.putText(frame, f"Movement status : {m_status}", (10, 60), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 3)
    cv2.putText(frame, f"Movement status : {m_status}", (10, 60), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
    return m_status

def endTheEdge(track_xyxy, i=0, edge_status=0):
    detections = []
    for det in track_xyxy:
        detections.append(det)
        if detections[i][0] < 10:
            edge_status = 1
            break
        else:
            edge_status = 0
        i += 1
    cv2.putText(frame, f"Edge status : {edge_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 3)
    cv2.putText(frame, f"Edge status : {edge_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
    print("Edge status in endTheEdge function : " + str(edge_status))
    return edge_status

def countSTB(track_xyxy, num_stb=0):
    for _ in track_xyxy:
        num_stb += 1
    cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 3)
    cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
    print("Numder(s) of STB in countSTB function : " + str(num_stb))
    return num_stb

def max_x1(track_xyxy,max_sublist=[]):
    if track_xyxy == []:
        pass
    else:
        max_sublist = max(track_xyxy, key=lambda x: x[0])
        cv2.rectangle(frame, (max_sublist[0], max_sublist[1]), (max_sublist[2], max_sublist[3]), (0, 0, 255), 2)
        print("MAX x1 : " + str(max_sublist))
    return max_sublist

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if success:
        results = model.track(source=frame, persist=True, iou=0.6, conf=0.5)

        track_xyxy = results[0].boxes.xyxy.int().cuda().tolist()
        print("Track xyxy :" + str(track_xyxy))

        if m_status == 1:
            max_sublist = max_x1(track_xyxy)
            num_stb = countSTB(track_xyxy)
            edge_status = endTheEdge(track_xyxy)
        elif m_status == 0:
            edge_status = 1
            cv2.putText(frame, f"Edge status : {edge_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 3)
            cv2.putText(frame, f"Edge status : {edge_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
            num_stb = countSTB(track_xyxy)
            max_sublist = max_x1(track_xyxy)
        
        m_status = movementStatus(track_xyxy, num_stb, edge_status)
        
        annotated_frame = results[0].plot()

        cv2.imshow("Annotaed Frame", annotated_frame)
        cv2.imshow("MAX x1", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        print("Can't read cap")
        break

cap.release()
cv2.destroyAllWindows()