import os
import csv
from natsort import natsorted

# Input directory
input_directory = '/home/Student/s4582342/LSE/data/train'

# Get a list of all video file names in the directory
video_files = [i for i in os.listdir(input_directory) if i.endswith('.mp4')]

# Sort the video file names in alphanumeric order
video_files = natsorted(video_files)

# Define the output CSV file
output_csv = '/home/Student/s4582342/LSE/data/train_labels.csv'

# Write the sorted video file names to the CSV file without headers
with open(output_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for filename in video_files:
        writer.writerow([filename, ""])

