import torch
from ultralytics import YOLO
from PIL import Image, ImageDraw

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if __name__ == "__main__":
    print("Running Inference on './test.jpg...'")
    detection_model = YOLO("yolov8m_UrduDoc.pt")
    input = Image.open("test.jpg")
    detection_results = detection_model.predict(source=input, conf=0.2, imgsz=1280, save=False, nms=True, device=device)
    bounding_boxes = detection_results[0].boxes.xyxy.cpu().numpy().tolist()
    bounding_boxes.sort(key=lambda x: x[1])
    
    draw = ImageDraw.Draw(input)
    for box in bounding_boxes:
        from numpy import random
        draw.rectangle(box, fill=None, outline=tuple(random.randint(0,255,3)), width=5)

    input.save("output.jpg")