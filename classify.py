from ultralytics import YOLO

# Load the models
car_incident_model = YOLO("Models/car_incident_trained_model.pt")
home_incident_model = YOLO("Models/home_incident_trained_model.pt")

# Path to the video
video_path = "Data/videos/route_incident/auto_20241003_090032.mp4"

# Run predictions on the video with each model
results_car = car_incident_model.predict(source=video_path, conf=0.4, vid_stride=5)
results_home = home_incident_model.predict(source=video_path, conf=0.4, vid_stride=5)

# Initialize confidence scores for both classes
car_confidence = 0
home_confidence = 0

# Aggregate confidence scores for all detections in car_incident_model
for box in results_car[0].boxes:
    car_confidence += box.conf.item()  # Sum up confidence scores

# Aggregate confidence scores for all detections in home_incident_model
for box in results_home[0].boxes:
    home_confidence += box.conf.item()  # Sum up confidence scores

print(f"Total confidence for car incident: {car_confidence:.2f}")
print(f"Total confidence for home incident: {home_confidence:.2f}")
# Predict which class the video belongs to
if car_confidence > home_confidence:
    print(f"This video is classified as a car incident with total confidence: {car_confidence:.2f}")
else:
    print(f"This video is classified as a home incident with total confidence: {home_confidence:.2f}")
