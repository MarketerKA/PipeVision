import cv2
from queue import Queue
import threading

# Define the pipes (queues) to hold the data between filters
pipe1 = Queue()
pipe2 = Queue()
pipe3 = Queue()
pipe4 = Queue()

# Function to capture video frames from a video file
def video_source(source):
    cap = cv2.VideoCapture(source)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        pipe1.put(frame)  # Send the frame to the first pipe
        cv2.waitKey(1)  # Small delay to simulate real-time processing
    cap.release()
    pipe1.put(None)  # End of stream signal

# Filter to convert the frame to grayscale
def black_and_white_filter():
    while True:
        frame = pipe1.get()
        if frame is None:
            pipe2.put(None)  # Pass the end signal to the next filter
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pipe2.put(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))  # Convert back to 3-channel BGR

# Filter to mirror the frame horizontally
def mirror_filter():
    while True:
        frame = pipe2.get()
        if frame is None:
            pipe3.put(None)  # Pass the end signal to the next filter
            break
        mirrored_frame = cv2.flip(frame, 1)  # Flip horizontally
        pipe3.put(mirrored_frame)

# Filter to resize the frame
def resize_filter():
    while True:
        frame = pipe3.get()
        if frame is None:
            pipe4.put(None)  # Pass the end signal to the next filter
            break
        resized_frame = cv2.resize(frame, (640, 480))  # Resize the frame
        pipe4.put(resized_frame)

# Filter to apply a custom effect (e.g., adding a blue tint)
def custom_effect_filter(output_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30  # Set this to the actual FPS of the input video
    width, height = 640, 480  # Output frame dimensions (matching resize_filter)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        frame = pipe4.get()
        if frame is None:
            break
        # Apply a blue tint effect
        blue_tint = frame.copy()
        blue_tint[:, :, 1] = blue_tint[:, :, 1] * 0.5  # Reduce the green channel
        blue_tint[:, :, 2] = blue_tint[:, :, 2] * 0.5  # Reduce the red channel
        out.write(blue_tint)  # Write processed frame to output video

    out.release()

# Main function to run the pipeline
def process_video(input_path, output_path):
    # Threads for each stage of the pipeline
    t1 = threading.Thread(target=video_source, args=(input_path,))
    t2 = threading.Thread(target=black_and_white_filter)
    t3 = threading.Thread(target=mirror_filter)
    t4 = threading.Thread(target=resize_filter)
    t5 = threading.Thread(target=custom_effect_filter, args=(output_path,))

    # Start all the threads
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
