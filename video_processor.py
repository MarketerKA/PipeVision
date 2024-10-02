import cv2
import numpy as np
from queue import Queue

# Define the pipes (queues) to hold the data between filters
pipe1 = Queue()
pipe2 = Queue()
pipe3 = Queue()
pipe4 = Queue()

# Function to capture video frames from a video file
def video_source(source='video.mp4'):
    cap = cv2.VideoCapture(source)  # Replace 'video.mp4' with the path to your video file
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        pipe1.put(frame)  # Pass frame to the first pipe
        cv2.waitKey(1)  # Small delay to make it real-time

    cap.release()
    pipe1.put(None)  # End of stream marker

# Filter to convert frame to grayscale
def black_and_white_filter():
    while True:
        frame = pipe1.get()  # Get frame from pipe1
        if frame is None:
            pipe2.put(None)
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pipe2.put(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))  # Convert back for consistency

# Filter to mirror the frame horizontally
def mirror_filter():
    while True:
        frame = pipe2.get()
        if frame is None:
            pipe3.put(None)
            break
        mirrored_frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        pipe3.put(mirrored_frame)

# Filter to resize the frame
def resize_filter():
    while True:
        frame = pipe3.get()
        if frame is None:
            pipe4.put(None)
            break
        resized_frame = cv2.resize(frame, (640, 480))  # Resize to 640x480
        pipe4.put(resized_frame)

# Filter to apply custom effect (e.g., adding a blue tint)
def custom_effect_filter():
    while True:
        frame = pipe4.get()
        if frame is None:
            break
        # Add a blue tint to the frame
        blue_tint = frame.copy()
        blue_tint[:, :, 1] = blue_tint[:, :, 1] * 0.5  # Reduce green channel
        blue_tint[:, :, 2] = blue_tint[:, :, 2] * 0.5  # Reduce red channel
        display_output(blue_tint)

# Function to display the final processed frame
def display_output(frame):
    cv2.imshow('Processed Video', frame)
    cv2.waitKey(1)

# Main function to run the pipeline
if __name__ == "__main__":
    # Start the video capture and the filter processing in sequence
    import threading

    # Threads for each filter
    t1 = threading.Thread(target=video_source, args=('video.mp4',))  # Provide the video file path
    t2 = threading.Thread(target=black_and_white_filter)
    t3 = threading.Thread(target=mirror_filter)
    t4 = threading.Thread(target=resize_filter)
    t5 = threading.Thread(target=custom_effect_filter)

    # Start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    # Clean up
    cv2.destroyAllWindows()
