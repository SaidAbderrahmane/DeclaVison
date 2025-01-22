from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("Models/yolov8l.pt")  # Load YOLOv8 Nano pre-trained model
    model.train(data="data.yaml", epochs=20, imgsz=640)
