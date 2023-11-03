import os
import cv2

# Input dataset
input_dataset = '/home/Student/s4582342/ConGD/data_old'

# Define the new resolution
new_width = 512
new_height = 512

# Resize each frame of each video sample to 512x512
# Generated by OpenAI's ChatGPT
def resize_videos_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".mp4"):
                input_video_path = os.path.join(root, filename)
                output_video_path = os.path.join(root, f"{os.path.splitext(filename)[0]}_resized.mp4")

                # Open the video capture
                cap = cv2.VideoCapture(input_video_path)

                # Get the current width and height of the video frames
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

                # Create a VideoWriter object to save the output video
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(output_video_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (new_width, new_height))

                # Iterate through the frames in the input video
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    # Resize the frame to the new resolution
                    frame = cv2.resize(frame, (new_width, new_height))

                    # Write the resized frame to the output video
                    out.write(frame)

                # Release the video capture and writer
                cap.release()
                out.release()

                print(f"Video '{filename}' resized and saved to '{output_video_path}'")

# Run function
resize_videos_in_directory(os.path.join(input_dataset, 'train'))
resize_videos_in_directory(os.path.join(input_dataset, 'val'))
resize_videos_in_directory(os.path.join(input_dataset, 'test'))
