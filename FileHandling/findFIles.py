import os

# Define the directory to search for files
directory = "/path/to/directory"

# Define the file extension to search for
file_extension = ".txt"  # Change this to the desired file extension

# List to store file paths with the specified extension
files_with_extension = []

# Iterate over files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(file_extension):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Add the file path to the list
            files_with_extension.append(file_path)

# Print the file paths with the specified extension
print("Files with extension", file_extension, "found:")
for file_path in files_with_extension:
    print(file_path)
