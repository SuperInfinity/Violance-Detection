from ultralytics import YOLO

# Load your model
model = YOLO('Models/yolov8n-pose.pt')

results = model(source="Data/v3.mp4", show=True, conf=0.4, save=True)
