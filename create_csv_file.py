import os
import csv

# Set the directory path where the folders are located
dir_path = "Mixer_Folder/Two_Combinations"

# Initialize an empty list to store the metadata
metadata = []

# Loop through each folder
for folder in os.listdir(dir_path):
    # Construct the full path to the folder
    folder_path = os.path.join(dir_path, folder)

    # Loop through each file in the folder
    for file in os.listdir(folder_path):
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file)

        # Add the file name and folder name to the metadata list
        metadata.append([file, folder])

# Define the path and filename for the CSV file
csv_file = "metadata.csv"

# Write the metadata list to the CSV file
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File Name", "Folder Name"])
    writer.writerows(metadata)
