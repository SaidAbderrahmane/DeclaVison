from ultralytics import YOLO
import logging
import os

import torch


if __name__ == "__main__":

    # print(torch.cuda.is_available())  # Should return True if GPU is available
    # print(torch.cuda.get_device_name(0))

    # Load a pre-trained YOLOv8 model
    model = YOLO("models/yolov8n.pt")

    # Get the full path to the downloaded dataset directory
    dataset_dir = "C:/Workspace/AI4Industry/DeclaVision/dataset_incident_maison/data.yaml"

    # Construct the full path to data.yaml
    # data_yaml_path = os.path.join(dataset_dir, "data.yaml")

    # Train the model using the full path to data.yaml
    results = model.train(data=dataset_dir, epochs=10, imgsz=640)

    logging.info(f"Process finished successfully!")