# pip install ultralytics

from ultralytics import YOLO

# Loading custom trained YOLO model
model = YOLO(r"./best.pt")

# Testing with an image
result = model(r"./fe8974f35fed4860.jpg")

# Show result
result[0].show()
