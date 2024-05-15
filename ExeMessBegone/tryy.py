# import customtkinter as ctk

# def home():
#     print("Home button clicked")

# def about():
#     print("About button clicked")

# def contact():
#     print("Contact button clicked")

# root = ctk.CTk()
# root.geometry("500x200")
# root.title("Vertical Navigation Bar")

# # Navbar Frame
# navbar_frame = ctk.CTkFrame(root, width=200, height=200)  # Increased width and height
# navbar_frame.pack(side="left", fill="y")
# navbar_frame.grid_propagate(False)  # Prevent frame from resizing based on content

# # Configure column to expand
# navbar_frame.columnconfigure(0, weight=1)

# # Button color
# button_color = "#FF5733"  # You can change this to any color you prefer

# # Navbar Buttons
# home_button = ctk.CTkButton(navbar_frame, text="Home", command=home, width=10)
# home_button.configure(bg=button_color)  # Set background color
# home_button.grid(row=0, column=0, sticky="ew", pady=(50, 5))  # Adding padding for vertical centering

# about_button = ctk.CTkButton(navbar_frame, text="About", command=about, width=10)
# about_button.configure(bg=button_color)  # Set background color
# about_button.grid(row=1, column=0, sticky="ew", pady=5)

# contact_button = ctk.CTkButton(navbar_frame, text="Contact", command=contact, width=10)
# contact_button.configure(bg=button_color)  # Set background color
# contact_button.grid(row=2, column=0, sticky="ew", pady=5)

# root.mainloop()
