import os
import csv

# Input csv and output csv, as well as input label file
input_csv = '/home/Student/s4582342/LSE/data/train_labels.csv'
output_csv = '/home/Student/s4582342/LSE/data/train_labels_final.csv'
input_label = '/home/Student/s4582342/LSE/train_old/MSSL_TRAIN_SET_GT_TXT'

# Create a dictionary to store label data
label_data = {}

# Read label data from the .txt files and store it in the dictionary
# Generated by OpenAI's ChatGPT
for txt_filename in os.listdir(input_label):
    if txt_filename.endswith('.txt'):
        base_filename = txt_filename[:8]  # Extract the first 8 characters
        with open(os.path.join(input_label, txt_filename), 'r') as label_file:
            label_lines = label_file.readlines()
            label_data[base_filename] = [line.strip() for line in label_lines]

# Read the original CSV file and create the updated CSV data
updated_csv_data = []
with open(input_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        filename = row[0][:8]  # Extract the first 8 characters of the filename
        if filename in label_data and label_data[filename]:
            # Update the second column with the label data
            row[1] = label_data[filename].pop(0)  # Remove and use the first label entry
        else:
            # If no label data is available or the label list is empty, leave the second column empty
            row[1] = ''
        updated_csv_data.append(row)

# Write the updated CSV data to the new CSV file
with open(output_csv, 'w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerows(updated_csv_data)