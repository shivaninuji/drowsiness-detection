from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
# Load the YOLO model (pretrained model)
model = YOLO('yolov5s.pt')  # Ensure 'yolo11x.pt' exists or use a different model

# Train the model
results = model.train(
    data="./configs/dataset.yaml",  # Dataset configuration file
    epochs=100,          # Number of training epochs
    imgsz=320,           # Image size
    batch=16,            # Batch size
    workers=4 ,      # Number of workers
    device='cpu'
)

print("Training completed!")