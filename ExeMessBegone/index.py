# import customtkinter
# import pywinstyles

# root = customtkinter.CTk()

# pywinstyles.apply_style(root, style="aero")
# root.title("hi")
# root.geometry("800x450")
# root.mainloop()
import customtkinter as ctk

class SidebarExample(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sidebar Example")
        self.geometry("800x600")

        # Create a frame for the sidebar
        self.sidebar_frame = ctk.Frame(self, width=200, bg="gray")
        self.sidebar_frame.pack(side="left", fill="y")

        # Create widgets for the sidebar
        self.button1 = ctk.Button(self.sidebar_frame, text="Button 1")
        self.button1.pack(fill="x", pady=10)

        self.button2 = ctk.Button(self.sidebar_frame, text="Button 2")
        self.button2.pack(fill="x", pady=10)

        # Create a frame for the main content
        self.main_frame = ctk.Frame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Create widgets for the main content
        self.label = ctk.Label(self.main_frame, text="Main Content", font=("Arial", 20))
        self.label.pack(pady=50, padx=100)

if __name__ == "__main__":
    app = SidebarExample()
    app.mainloop()
