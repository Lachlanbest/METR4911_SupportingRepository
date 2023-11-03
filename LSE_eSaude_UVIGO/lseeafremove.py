import os

# Input directory
input_directory = '/home/Student/s4582342/LSE/train/MSSL_TRAIN_SET_VIDEOS_ELAN'

# List all files in the directory
files = os.listdir(input_directory)

# Remove files ending in .eaf
for file in files:
    if file.endswith('.eaf'):
        file_path = os.path.join(input_directory, file)
        try:
            os.remove(file_path)
            print(f"Removed file: {file}")
        except OSError as e:
            print(f"Error removing file: {file} - {e}")
