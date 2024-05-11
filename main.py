# File cleaner
# 1]Clean exe file 
# 2]Sort coding files 
# 3]Speed Boost

import os
import time
import keyboard
import shutil
import tkinter as tk
from tkinter import filedialog


# Introduction
introduction = "Hi there! I'm ExeMess Begone! Tired of all those messy executables cluttering up your computer? Well, fear not! With me around, you can say goodbye to the chaos and hello to a tidier system in no time!"

# introduction2 = introduction.split()

for i in introduction:
    for j in i:
        print(j, end="", flush=True)
        time.sleep(0.01)
    print("", end="", flush=True)



# 3 functions - one for search second for deletion and 3rd for to choose 


# 1.2 Option for deleting files
def deleteExe(fileList):
    print("Press Enter to Confirm or Ctrl + c To Terminate")
    keyboard.wait("Enter")
    for f in fileList:
        os.remove(f)
        print(f + " removed")




#First Module (Clean .exe Files)
def searchExe():
    directory = "C:/Users/Admin/Downloads/"
    file_extension = "   " #your extension goes here!
    fileList = []

    print("Wait for few seconds...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                filePath = os.path.join(root, file)
                fileList.append(filePath)


    print("\n\nFiles found:")
    for i in fileList:
        print(i)

    ch = input("Are we sure to remove all files from your PC!? (y/n)")
    if ch == "y":
        deleteExe(fileList)
    elif ch == "n":
        print("Yes Sure! No problem. Have a good day.")
    else:
        print("Invalid Input! Please enter y/n")
        


#Sorting all code files
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











# Choice for all 3 modules
def options():
    print("\n1. Check all .exe files and remove it!")
    print("2. Sort all your programming files")
    print("3. Boost your memory")
    print("")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        searchExe()
    elif choice == 2:
        sortCodeFiles()
    elif choice == 3:
        boostMemory()
    else:
        print("Invalid choice!")

options()



