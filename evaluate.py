from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("Models/best.pt")  # Replace with your model path

    # Validate model on test set
    metrics = model.val(data="data.yaml", split="test")
    print(metrics)
