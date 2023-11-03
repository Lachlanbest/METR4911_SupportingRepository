import os
import pandas as pd

# Generated by OpenAI's ChatGPT
# Define the directory containing your video files
video_dir = '/home/Student/s4582342/data/train'  # Replace with the actual path to your video directory

# Define the path to your CSV file
csv_file = '/home/Student/s4582342/data_old/train_labels.csv'  # Replace with the actual path to your CSV file

# Check if the video directory exists
if not os.path.exists(video_dir):
    print(f"Video directory '{video_dir}' does not exist.")
    exit()

# Check if the CSV file exists
if not os.path.exists(csv_file):
    print(f"CSV file '{csv_file}' does not exist.")
    exit()

# Read the CSV file into a DataFrame without headers
df = pd.read_csv(csv_file, header=None, names=['filename', 'gesture_label'])

# Create an empty DataFrame to store the filtered data
filtered_df = pd.DataFrame(columns=df.columns)

# Iterate through each row in the original DataFrame
for index, row in df.iterrows():
    video_filename = row['filename']
    video_path = os.path.join(video_dir, video_filename)

    # Check if the video file exists
    if os.path.exists(video_path):
        filtered_df = filtered_df.append(row, ignore_index=True)

# Define the path for the new filtered CSV file
filtered_csv_file = '/home/Student/s4582342/data/train_labels.csv'  # Replace with the desired output path

# Save the filtered DataFrame to the new CSV file without headers
filtered_df.to_csv(filtered_csv_file, index=False, header=False)

print(f"Filtered CSV file saved to '{filtered_csv_file}'.")
