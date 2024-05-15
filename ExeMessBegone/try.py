import pywinstyles
import customtkinter as ctk
from tkinter.colorchooser import askcolor
import tkinter

root = ctk.CTk()
root.geometry("700x500")
root.title("ExE BE-GonE")
# ctk.set_appearance_mode("dark")
pywinstyles.apply_style(root, "aero")
pywinstyles.change_header_color(root, color="blue")

navbar_frame = ctk.CTkFrame(root, width=180, fg_color="#0d0d0d")
navbar_frame.pack(side="left", fill="y")
navbar_frame.grid_propagate(False)

# button_color = "#FF5733"
# ctk.set_button_style(bg=button_color)
# pywinstyles.set_button_style(root,bg=button_color)


exe_button = ctk.CTkButton(navbar_frame ,text="Exe Cleaner", width=100, fg_color="#8c8c8c")
exe_button.grid(sticky="ew", pady=(140, 10), padx=40)
# exe_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

sort_button = ctk.CTkButton(navbar_frame, text="Sort your files", width=100, fg_color="#8c8c8c")
sort_button.grid(sticky="ew", pady=10, padx=40)

# pywinstyles.set_opacity(exe_button, value=0.5) 

# sort_button.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)


# button = customtkinter.CTkButton(master=root_tk,
#                                  fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
#                                  text="CTkButton",
#                                  command=button_event)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()