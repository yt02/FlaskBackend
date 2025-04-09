
from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

def detect_objects(image_path):
    results = model(image_path)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            detections.append({
                "label": label,
                "confidence": conf,
                "box": [x1, y1, x2, y2]
            })

    return detections
