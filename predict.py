from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("Models/best.pt") 

    # Predict on new video or images
    results = model.predict(source="new_video.mp4", save=True)
    print(results)
