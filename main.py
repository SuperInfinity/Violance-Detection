from ultralytics import YOLO

model_name = "Models/yolo-violence.pt"

model = YOLO(model_name)

result = model(source="Data/1.jpg", show=True, conf=0.4, save=False)

for i in result:
    print(i)


