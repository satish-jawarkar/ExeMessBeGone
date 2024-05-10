import os
import shutil

# Define the source directory containing the files
source_dir = "/path/to/source/directory"

# Define the destination directory where files will be sorted
destination_dir = "/path/to/destination/directory"

# Define the file extension to sort
file_extension = ".txt"  # Change this to the desired file extension

# Iterate over files in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith(file_extension):
        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        # Define the full source and destination paths
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)
        # Move the file to the destination directory
        shutil.move(source_path, destination_path)
        print(f"Moved {file_name} to {destination_dir}")
