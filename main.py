
from matplotlib import pyplot as plt
import cv2
import uuid   # Unique identifier
import os
import time

# Load YOLO model (optional, not used in this script)


# Directory for saving images
IMAGES_PATH = os.path.join('data', 'images') 
labels = ['awake', 'drowsy']
number_imgs = 20

# Ensure directory exists
if not os.path.exists(IMAGES_PATH):
    os.makedirs(IMAGES_PATH)

# Open webcam
cap = cv2.VideoCapture(1)

# Check if webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    # Loop through labels
    for label in labels:
        print('Collecting images for {}'.format(label))
        time.sleep(5)  # 5-second delay to prepare for each label
        
        # Loop through image range
        for img_num in range(number_imgs):
            print(f'Collecting images for {label}, image number {img_num}')
            
            # Capture webcam frame
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture image")
                continue
            
            # Generate unique filename
            imgname = os.path.join(IMAGES_PATH, f"{label}.{uuid.uuid1()}.jpg")
            
            # Save the image
            cv2.imwrite(imgname, frame)
            print(f"Image saved to: {imgname}")
            
            # Show the frame on screen
            cv2.imshow('Image Collection', frame)
            
            # 2-second delay between captures
            time.sleep(2)
            
            # Break on 'q' key press
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
finally:
    cap.release()
    cv2.destroyAllWindows()



