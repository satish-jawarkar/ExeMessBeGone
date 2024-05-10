import tkinter as tk
from tkinter import filedialog
import os
import shutil

def sortCodeFiles():
    root = tk.Tk()
    root.withdraw()
    print("Choose source folder")
    source_dir = filedialog.askdirectory()
    root.destroy()

    destination_dir = r"C:\Users\Admin\Desktop\Codefiles"

    extension = input("Enter file extension using .")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for file_name in os.listdir(source_dir):
        if file_name.endswith(extension):
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    print("All files are sorted!")

# Call the function to sort code files
sortCodeFiles()
