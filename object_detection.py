import streamlit as st
import cv2
import pyttsx3
import time
from ultralytics import YOLO
import winsound

# Load the custom YOLO model
custom_model = YOLO('/configs/best.pt')  # Adjust this path

# Initialize voice engine using pyttsx3
engine = pyttsx3.init()

# To track drowsiness status
drowsy_time = 0
drowsy_threshold = 10  # In seconds
alarm_playing = False  # Track if alarm is currently playing
last_alert_time = 0  # To track when the last alert was spoken

# Streamlit UI
st.title("Drowsiness Detection")
st.write("This application detects drowsiness using the webcam. If you are detected as drowsy for more than 10 seconds, an alert will sound.")

# Create a placeholder for the webcam feed
webcam_placeholder = st.empty()

# Function to check if the person is drowsy
def check_drowsiness(frame):
    global drowsy_time

    # Run inference on the frame (ensure it's the correct input type)
    custom_results = custom_model(frame)

    # Check if drowsiness is detected
    drowsy_detected = False
    for result in custom_results:
        for box in result.boxes:
            class_name = custom_model.names[int(box.cls[0])]
            if class_name == "drowsy":  # Check if the detected class is 'drowsy'
                drowsy_detected = True
                break
    
    if drowsy_detected:
        drowsy_time += 1
    else:
        drowsy_time = 0  # Reset if not drowsy

    return drowsy_detected

# Function to handle voice alert using pyttsx3
def speak_alert():
    engine.say("Warning! You are drowsy. Please take a break!")
    engine.runAndWait()

# Function to play an alarm sound (using winsound or any other method)
def play_alarm():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 ms = 1 second
    winsound.Beep(frequency, duration)

# Main webcam and detection loop
cap = cv2.VideoCapture(1)  # Use the default webcam (0 refers to the first connected camera)
if not cap.isOpened():
    st.error("Could not access the webcam. Please ensure your camera is connected.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame. Please try again.")
            break

        # Check for drowsiness
        drowsy_detected = check_drowsiness(frame)

        # If drowsiness is detected and threshold is met, and it's not already playing
        if drowsy_detected and drowsy_time >= drowsy_threshold:
            current_time = time.time()  # Get the current time
            
            # Only repeat the alert every 5 seconds to avoid too many repetitions
            if not alarm_playing or (current_time - last_alert_time > 5):  # 5 seconds delay
                play_alarm()
                speak_alert()
                alarm_playing = True  # Set the flag to indicate alarm is playing
                last_alert_time = current_time  # Update the time when the last alert was spoken

        # If the person is awake, stop the alarm
        elif not drowsy_detected and alarm_playing:
            alarm_playing = False  # Stop the alarm when awake

        # Convert frame to RGB for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Update the session state with the current frame
        st.session_state.frame = frame_rgb

        # Display the frame in Streamlit
        webcam_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)


        # Add a delay to control frame rate
        time.sleep(1)

    cap.release()