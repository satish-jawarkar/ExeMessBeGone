import customtkinter as ctk
from tkinter import filedialog
import os
import shutil
import threading
import itertools
import time
import tkinter

root = ctk.CTk()
root.geometry("700x500")
root.title("ExE BE-GonE")

# Define fonts
default_font = ("Comic Sans MS", 12)
button_font = ("Comic Sans MS", 12)
input_font = ("Comic Sans MS", 12)

output_label = None
input_entry = None
animation_label = None
confirm_button = None
source_entry = None
extension_entry = None
move_copy_choice = None
move_radio = None
copy_radio = None

# Utility Functions
def clear_screen():
    global output_label, input_entry, animation_label, confirm_button
    for widget in scrollable_frame.winfo_children():
        widget.pack_forget()
    output_label.configure(text="")
    input_entry.pack_forget()
    animation_label.configure(text="")
    confirm_button.pack_forget()

def start_animation():
    def animate():
        loading_text = itertools.cycle(["Loading.", "Loading..", "Loading...", "Loading...."])
        def update_text():
            animation_label.configure(text=next(loading_text))
            animation_label.after_id = animation_label.after(300, update_text)
        update_text()
    threading.Thread(target=animate).start()

def stop_animation():
    animation_label.after_cancel(animation_label.after_id)
    animation_label.configure(text="")

# Exe Cleaner Functions
def deleteExe(fileList):
    global output_label, input_entry, confirm_button
    output_label.configure(text="Press 'Confirm' to remove the files or 'Cancel' to terminate")

    def perform_deletion():
        for f in fileList:
            os.remove(f)
            current_text = output_label.cget("text")
            output_label.configure(text=f"{current_text}\n{f} removed")
        output_label.configure(text=f"{current_text}\nAll selected files removed")

    confirm_button.configure(command=perform_deletion)
    confirm_button.pack(side="bottom", pady=10, padx=20)

def searchExe():
    global output_label, input_entry, animation_label, confirm_button
    clear_screen()
    directory = "C:/Users/Admin/Downloads/"
    file_extension = ".exe"
    fileList = []

    output_label.configure(text="Please wait for a few seconds...")
    start_animation()

    def perform_search():
        for root_dir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    filePath = os.path.join(root_dir, file)
                    fileList.append(filePath)
                    current_text = output_label.cget("text")
                    output_label.configure(text=f"{current_text}\n{filePath}")
                    time.sleep(0.3)
        stop_animation()
        output_label.configure(text=f"{output_label.cget('text')}\n\nAre we sure to remove all files from your PC!? (y/n)")
        input_entry.pack(side="bottom", pady=10, padx=20, anchor="s")

        confirm_button.configure(command=lambda: get_user_input(fileList))
        confirm_button.pack(side="bottom", pady=10, padx=20)

    threading.Thread(target=perform_search).start()

def get_user_input(fileList):
    global input_entry, output_label
    ch = input_entry.get().strip().lower()
    input_entry.delete(0, 'end')
    if ch == "y":
        deleteExe(fileList)
    elif ch == "n":
        output_label.configure(text="Yes Sure! No problem. Have a good day.")
    else:
        output_label.configure(text="Invalid Input! Please enter y/n")

# Sorting Code Files Functions
def choose_source_directory():
    root_dir = tkinter.Tk()
    root_dir.withdraw()
    source_dir = filedialog.askdirectory()
    root_dir.destroy()
    source_entry.delete(0, 'end')
    source_entry.insert(0, source_dir)

def sortCodeFiles():
    global source_entry, extension_entry, move_copy_choice, output_label, confirm_button
    clear_screen()

    source_entry.pack(pady=10, padx=20, fill="x")
    browse_button.pack(pady=10, padx=20)
    extension_entry.pack(pady=10, padx=20, fill="x")
    move_radio.pack(pady=5, padx=20)
    copy_radio.pack(pady=5, padx=20)

    def perform_sort():
        source_dir = source_entry.get()
        if not source_dir:
            output_label.configure(text="Please choose a source directory")
            return

        extension = extension_entry.get().strip()
        if not extension.startswith('.'):
            extension = '.' + extension

        move_copy = move_copy_choice.get()
        if move_copy not in ["m", "c"]:
            output_label.configure(text="Please choose a valid option to move or copy files")
            return

        destination_dir = r"C:\Users\Admin\Desktop\Codefiles"
        folder_name = f"All {extension} Files"
        folder_path = os.path.join(destination_dir, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        fileList = [f for f in os.listdir(source_dir) if f.endswith(extension)]

        for file_name in fileList:
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(folder_path, file_name)
            if move_copy == "m":
                shutil.move(source_path, destination_path)
                output_label.configure(text=f"{output_label.cget('text')}\nMoved: {file_name}")
            elif move_copy == "c":
                shutil.copy(source_path, destination_path)
                output_label.configure(text=f"{output_label.cget('text')}\nCopied: {file_name}")

        output_label.configure(text=f"All files are sorted at {folder_path}")

    confirm_button.configure(command=perform_sort)
    confirm_button.pack(side="bottom", pady=10, padx=20)

# Navbar Frame
navbar_frame = ctk.CTkFrame(root, width=180, fg_color="#0d0d0d")
navbar_frame.pack(side="left", fill="y")
navbar_frame.grid_propagate(False)

# Navbar Buttons
exe_button = ctk.CTkButton(navbar_frame, text="Exe Cleaner", width=100, fg_color="#8c8c8c", command=searchExe)
exe_button.configure(font=button_font)
exe_button.grid(sticky="ew", pady=(140, 10), padx=40)

sort_button = ctk.CTkButton(navbar_frame, text="Sort your files", width=100, fg_color="#8c8c8c", command=sortCodeFiles)
sort_button.configure(font=button_font)
sort_button.grid(sticky="ew", pady=10, padx=40)

# Output Frame
scrollable_frame = ctk.CTkScrollableFrame(root, fg_color="#1a1a1a")
scrollable_frame.pack(side="right", fill="both", expand=True)

output_label = ctk.CTkLabel(scrollable_frame, text="", fg_color="#1a1a1a", text_color="white", anchor="nw", font=default_font)
output_label.pack(pady=20, padx=20, fill="both", expand=True)

animation_label = ctk.CTkLabel(scrollable_frame, text="", fg_color="#1a1a1a", text_color="white", anchor="s", font=default_font)
animation_label.pack(side="bottom", pady=10, padx=20, anchor="s")

input_entry = ctk.CTkEntry(scrollable_frame, font=input_font)
confirm_button = ctk.CTkButton(scrollable_frame, text="Confirm")

# Input Elements for Sort Code Files
source_entry = ctk.CTkEntry(scrollable_frame, font=input_font)
browse_button = ctk.CTkButton(scrollable_frame, text="Browse", command=choose_source_directory)
extension_entry = ctk.CTkEntry(scrollable_frame, font=input_font)
move_copy_choice = ctk.StringVar(value="m")
move_radio = ctk.CTkRadioButton(scrollable_frame, text="Move", variable=move_copy_choice, value="m")
copy_radio = ctk.CTkRadioButton(scrollable_frame, text="Copy", variable=move_copy_choice, value="c")

root.mainloop()
