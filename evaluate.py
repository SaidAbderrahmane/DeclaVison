from ultralytics import YOLO
import os
from IPython.display import Video


if __name__ == "__main__":
    # model = YOLO("Models/best.pt")  # Replace with your model path

    # # Validate model on test set
    # metrics = model.val(data="data.yaml", split="test")
    # print(metrics)


    # Load the trained model
    model = YOLO('runs/detect/train4/weights/best.pt')

    video_path = "Data/videos/home_incident/IMG_4775 2.MOV"

    # Extract directory and filename of the original video
    video_dir, video_filename = os.path.split(video_path)
    video_name, video_ext = os.path.splitext(video_filename)

    # Construct the output video path with the suffix, in the same directory
    output_video_path = os.path.join(video_dir, f"{video_name}_result{video_ext}")

    # Run inference and save the results with the specified output path
    results = model(source=video_path, conf=0.4, save=True, save_dir=video_dir, name=f"{video_name}_result")