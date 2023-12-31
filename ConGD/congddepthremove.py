import os

# Input dataset
input_dataset = '/home/Student/s4582342/ConGD/data'

# Delete .mp4 files with 'K' in the filename but keep 'M' files
# Generated by OpenAI's ChatGPT
def delete_files_with_k(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.lower().endswith('.mp4') and 'K' in filename:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

# Iterate through the training, validation, and test splits
splits = ['train', 'val', 'test']
for split in splits:
    split_dir = os.path.join(input_dataset, split)

    # Check if the split directory exists
    if not os.path.exists(split_dir):
        continue

    # Iterate through gesture class directories within the split
    for gesture_class in os.listdir(split_dir):
        gesture_class_dir = os.path.join(split_dir, gesture_class)

        # Check if the gesture class directory exists
        if not os.path.isdir(gesture_class_dir):
            continue

        # Delete .mp4 files with 'K' in the filename but keep 'M' files in the gesture class directory
        delete_files_with_k(gesture_class_dir)
