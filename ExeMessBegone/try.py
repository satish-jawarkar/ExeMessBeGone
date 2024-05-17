import pywinstyles
import customtkinter as ctk
from tkinter.colorchooser import askcolor
import tkinter
import os
import time
import keyboard
import shutil
# import tkinter as tk
from tkinter import filedialog
import threading
import itertools
from tkinter import font

root = ctk.CTk()
root.geometry("700x500")
root.title("ExE BE-GonE")
# ctk.set_appearance_mode("dark")
pywinstyles.apply_style(root, "aero")
pywinstyles.change_header_color(root, color="blue")
output_label = None
input_entry = None
animation_label = None

# Define fonts
default_font = ("Comic Sans MS", 12)
button_font = ("Comic Sans MS", 12)
input_font = ("Comic Sans MS", 12)

def deleteExe(fileList):
    global output_label, input_entry
    output_label.configure(text="Press Enter to Confirm or Ctrl + C to Terminate")
    
    def wait_for_enter():
        input_entry.bind("<Return>", lambda e: perform_deletion(fileList))
        input_entry.focus()

    def perform_deletion(fileList):
        for f in fileList:
            os.remove(f)
            current_text = output_label.cget("text")
            output_label.configure(text=f"{current_text}\n{f} removed")
        output_label.configure(text=f"{current_text}\nAll selected files removed")

    threading.Thread(target=wait_for_enter).start()

def searchExe():
    global output_label, input_entry, animation_label
    directory = "C:/Users/Admin/Downloads/"
    file_extension = ".exe"  # Example extension
    fileList = []

    output_label.configure(text="Please wait for a few seconds...")
    start_animation()

    def stop_animation():
        animation_label.after_cancel(animation_label.after_id)
        animation_label.configure(text="")

    def perform_search():
        for root_dir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    filePath = os.path.join(root_dir, file)
                    fileList.append(filePath)
                    current_text = output_label.cget("text")
                    output_label.configure(text=f"{current_text}\n{filePath}")
                    time.sleep(0.3)  # Delay to show files one by one
        stop_animation()

        current_text = output_label.cget("text")
        def confirm_deletion():
            output_label.configure(text=f"{current_text}\n\nAre we sure to remove all files from your PC!? (y/n)")
            input_entry.pack(side="bottom", pady=10, padx=20, anchor="s")
            input_entry.bind("<Return>", lambda e: get_user_input(fileList))

        threading.Thread(target=confirm_deletion).start()

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

def start_animation():
    def animate():
        loading_text = itertools.cycle(["Loading.", "Loading..", "Loading...", "Loading...."])
        def update_text():
            animation_label.configure(text=next(loading_text))
            animation_label.after_id = animation_label.after(300, update_text)
        update_text()
    threading.Thread(target=animate).start()

# Navbar Frame
navbar_frame = ctk.CTkFrame(root, width=180, fg_color="#0d0d0d")
navbar_frame.pack(side="left", fill="y")
navbar_frame.grid_propagate(False)

# Navbar Buttons
exe_button = ctk.CTkButton(navbar_frame, text="Exe Cleaner", width=100, fg_color="#8c8c8c", command=searchExe)
exe_button.configure(font=button_font)
exe_button.grid(sticky="ew", pady=(140, 10), padx=40)

sort_button = ctk.CTkButton(navbar_frame, text="Sort your files", width=100, fg_color="#8c8c8c")
sort_button.configure(font=button_font)
sort_button.grid(sticky="ew", pady=10, padx=40)

# Output Frame
scrollable_frame = ctk.CTkScrollableFrame(root, fg_color="#1a1a1a")  # Dark background color
scrollable_frame.pack(side="right", fill="both", expand=True)

output_label = ctk.CTkLabel(scrollable_frame, text="", fg_color="#1a1a1a", text_color="white", anchor="nw", font=default_font)
output_label.pack(pady=20, padx=20, fill="both", expand=True)

animation_label = ctk.CTkLabel(scrollable_frame, text="", fg_color="#1a1a1a", text_color="white", anchor="s", font=default_font)
animation_label.pack(side="bottom", pady=10, padx=20, anchor="s")

input_entry = ctk.CTkEntry(scrollable_frame, font=input_font)
# pywinstyles.set_opacity(exe_button, value=0.5) 

# sort_button.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)


# button = customtkinter.CTkButton(master=root_tk,
#                                  fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
#                                  text="CTkButton",
#                                  command=button_event)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()