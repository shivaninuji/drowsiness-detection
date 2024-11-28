# Drowsiness Detection System

This project implements a **Drowsiness Detection System** using real-time computer vision techniques to monitor whether a person is awake or drowsy. It is primarily designed for real-time scenarios such as driving and studying, where the person may become drowsy. The system raises an alert when it detects drowsiness, playing an alarm sound and providing a voice warning. This can help prevent accidents during driving and improve productivity while studying.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Training the Model](#training-the-model)


## Features

- Real-time drowsiness detection using webcam input.
- Alarm and voice alerts after detecting 10 counts of drowsiness. (the number of counts can be varied)
- Continuous monitoring: If drowsiness is detected again, the counter resets.
- Can be used for drivers and students to ensure they stay alert.
- Custom-trained YOLOv5 model to detect drowsiness.
- Frontend implemented with Streamlit for easy interaction.


## Technologies Used

- **Python**: Main programming language.
- **OpenCV**: For video capture and image processing.
- **YOLOv5 (Ultralytics)**: Custom-trained object detection model for drowsiness detection.
- **Streamlit**: For building the user interface and visualizing the output.
- **pyttsx3**: For voice alerts when drowsiness is detected.
- **LabelImg**: Used for image annotation during dataset creation.


## Installation Guide

### 1. Clone the repository:

```bash
git clone https://github.com/shivaninuji/drowsiness-detection.git
cd drowsiness-detection
```

### 2. Create a virtual environment and activate the virtual environment:

```bash
venv\Scripts\activate
```

### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```


## Usage

1. Run the Streamlit app:

```bash
streamlit run object_detection.py
```

2. The app will open in your browser. Make sure your webcam is connected and accessible.

3. The application will monitor your webcam feed for signs of drowsiness. When drowsiness is detected, the system will beep and announce a voice alert: "Warning! You are drowsy. Please take a break!"

4. The alert will continue until the system detects that the user is awake, or if drowsiness is detected again, it will reset the counter.


## Training the Model

To train the YOLOv5 model for drowsiness detection:

1. **Prepare the dataset**: Capture images of a person in a drowsy and awake state. Label the images using **LabelImg**. 
   - Each image should have a unique ID.
   - Create two classes: "drowsy" and "awake" (or any other labels you deem appropriate).

2. **Create a YAML file** for your dataset:
   - The file should include paths to the images and labels.
   - Example:
     ```yaml
     path: "./data"
     train: images
     val: images
     test: # test images (optional)
     nc: 17
     names : ['dog', 'person', 'cat', 'tv', 'car', 'meatballs', 'marinara sauce', 'tomato soup', 'chicken noodle soup', 'french onion soup', 'chicken breast', 'ribs', 'pulled pork', 'hamburger', 'cavity', 'awake', 'drowsy']
     ```

3. **Train the model**:
   - Run the `test.py` file to train the model.

4. **Use the trained model**:
   - Once training is complete, use the model weights (`best.pt`) to detect drowsiness in real-time using the webcam.
