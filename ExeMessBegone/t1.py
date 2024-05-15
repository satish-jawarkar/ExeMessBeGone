import customtkinter
from ctypes import windll
from PIL import Image, ImageTk
import os

# Template Options
class CTkWindow(customtkinter.CTk):
    def __init__(self,
                app_title = "CTk", # Application name
                geometry = "500x300", # Enter window geometry 
                titlebar_color = "default", # Specify the color of top bar
                title_color = "default", # Title label color
                focus_out_color = "default", # default focus out header color
                fg_color = "default", # fg_color of window
                resizable = True, # Resize window dynamically
                round_corner = 12, # corner_radius
                icon = None, # icon path
                justify = "left", # title justify
                style = "modern" # style -modern/classic
                ):
        
        super().__init__()
        self.overrideredirect(1)
        transparent_color = self._apply_appearance_mode(['#f2f2f2','#000001'])
        self.config(background=transparent_color)
        self.attributes("-transparentcolor", transparent_color) # transparent_color will be the transparent color
        self.geometry(geometry)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self.fullscreen = False
        self.GWL_EXSTYLE = -20
        self.WS_EX_APPWINDOW = 0x00040000
        self.WS_EX_TOOLWINDOW = 0x00000080
        self.titlebar_color = ["white","black"] if titlebar_color=="default" else titlebar_color
        title_color = ["black","white"] if title_color=="default" else title_color
        self.focus_out_color = ["white", "#2b2b2b"] if focus_out_color=="default" else focus_out_color
        
        self.header = customtkinter.CTkFrame(self, corner_radius=round_corner, fg_color=self.titlebar_color,
                                           background_corner_colors=(transparent_color,transparent_color,None,None))
        self.header.grid(sticky="nwe", row=0)
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid_rowconfigure(0, weight=1)
        self.header.bind("<ButtonPress-1>", self.oldxyset)
        self.header.bind("<B1-Motion>",  self.move_window)
        self.header.bind("<Double-1>",  lambda e: self.max_window())
        self.bind("<FocusOut>", lambda e: self.header.configure(fg_color=self.focus_out_color))
        self.bind("<FocusIn>", lambda e: self.header.configure(fg_color=self.titlebar_color))
        
        fg_color = customtkinter.ThemeManager.theme["CTk"]["fg_color"] if fg_color=="default" else fg_color
            
        self.app = customtkinter.CTkFrame(self, corner_radius=round_corner, bg_color=transparent_color, fg_color=fg_color,
                                     background_corner_colors=(fg_color,fg_color,None,None))
        self.app.grid(sticky="nsew", row=0,pady=(29,0))
        self.app.bind("<Map>", self.frame_mapped)
        
        if resizable==True:
            self.app.bind("<Motion>", self.change_cursor)
            self.app.bind("<B1-Motion>", self.resize)
            max_button_color = "yellow"
            hover_color = "#ffda71"
        else:
            max_button_color = "grey60"
            hover_color = "grey60"
            
        self.resizable = resizable
        self.ctkimage = customtkinter.CTkImage(Image.open(os.path.join(os.path.dirname(customtkinter.__file__),"assets","icons","CustomTkinter_icon_Windows.ico")), size=(16,16))
        self.icon = self.ctkimage if icon is None else customtkinter.CTkImage(Image.open(icon), size=(16,16))
        self.title_label = customtkinter.CTkLabel(self.header, width=10, image=self.icon, compound="left", text=f"  {app_title}", anchor="n", text_color=title_color)
        if justify=="center":
            self.title_label.grid(row=0, sticky="we", padx=(30,0), pady=7)
        else:
            self.title_label.grid(row=0, sticky="w", padx=8, pady=7)
         
        self.title_label.bind("<ButtonPress-1>", self.oldxyset)
        self.title_label._label.bind("<ButtonPress-1>", self.oldxyset)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind("<Double-1>",  lambda e: self.max_window())
        self.minmize = False
        self.style = style
        if style=="modern":
            self.button_close = customtkinter.CTkButton(self.header, corner_radius=10, width=10, height=10, text="",
                                                   hover_color="dark red", fg_color="red", command=self.close_window)
            self.button_close.grid(row=0, column=2, sticky="ne", padx=(0,15), pady=10)
            self.button_close.configure(cursor="arrow")

            self.button_max = customtkinter.CTkButton(self.header, corner_radius=10, width=10, height=10, text="",
                                                 hover_color=hover_color, fg_color=max_button_color, command=self.max_window)
            self.button_max.grid(row=0, column=1, sticky="ne", padx=10, pady=10)
            self.button_max.configure(cursor="arrow")

            self.button_min = customtkinter.CTkButton(self.header, corner_radius=10, width=10, height=10, text="",
                                                 hover_color="light green", fg_color="green", command=self.min_window)
            self.button_min.grid(row=0, column=0, sticky="ne", pady=10)
            self.button_min.configure(cursor="arrow")
        else:
            self.button_close = customtkinter.CTkButton(self.header, corner_radius=round_corner, width=40, height=30, text="✕",
                                                   hover_color="#c42b1c", fg_color="transparent", text_color=["black","white"],
                                                   background_corner_colors=(None,transparent_color,None,None), command=self.close_window)
            self.button_close.grid(row=0, column=2, sticky="ne", padx=0, pady=0)
            self.button_close.configure(cursor="arrow")
            self.button_close.bind("<Enter>", lambda e: self.change_bg(transparent_color, 1), add="+")
            self.button_close.bind("<Leave>", lambda e: self.change_bg(transparent_color, 0), add="+")
            
            self.button_max = customtkinter.CTkButton(self.header, corner_radius=0, width=40, height=30, text="□",text_color=["black","white"],
                                                 hover_color="#2d2d2d", fg_color="transparent", command=self.max_window)
            self.button_max.grid(row=0, column=1, sticky="ne", padx=0, pady=0)
            self.button_max.configure(cursor="arrow")

            self.button_min = customtkinter.CTkButton(self.header, corner_radius=0, width=40, height=30, text="�"",text_color=["black","white"],
                                                 hover_color="#2d2d2d", fg_color="transparent", command=self.min_window)
            self.button_min.grid(row=0, column=0, sticky="ne", pady=0)
            self.button_min.configure(cursor="arrow")

    def change_bg(self, transparent_color, hover):
        if hover: 
            self.button_close.configure(background_corner_colors=("#c42b1c",transparent_color,"#c42b1c","#c42b1c"), fg_color="#c42b1c")
        else:
            self.button_close.configure(background_corner_colors=(self.titlebar_color,transparent_color,self.titlebar_color,self.titlebar_color),
                                        fg_color=self.titlebar_color)
            
    def geometry(self, geometry):
        super().geometry(geometry)
        
    def iconbitmap(self, icon):
        self.icon = customtkinter.CTkImage(Image.open(icon), size=(16,16))
        self.title_label.configure(image=self.icon)
        
    def oldxyset(self, event):
        self.oldx = event.x
        self.oldy = event.y
        
    def move_window(self, event):
        if self.fullscreen==False:
            self.y = event.y_root - self.oldy
            self.x = event.x_root - self.oldx
            self.geometry(f'+{self.x}+{self.y}')
        
    def close_window(self):
        super().destroy()
        
    def frame_mapped(self, e):
        self.update_idletasks()
        self.overrideredirect(True)
        self.state('normal')
        if self.minmize:
            self.fullscreen = False
            self.max_window()
        self.minmize = False
        
    def min_window(self):
        self.update_idletasks()
        self.overrideredirect(False)
        self.withdraw()
        self.state('iconic')
        if self.fullscreen:
            self.minmize = True
        
    def set_appwindow(self):
        hwnd = windll.user32.GetParent(self.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, self.GWL_EXSTYLE)
        style = style & ~self.WS_EX_TOOLWINDOW
        style = style | self.WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, self.GWL_EXSTYLE, style)
        self.wm_withdraw()
        self.after(10, lambda: self.wm_deiconify())
        
    def max_window(self):
        if self.resizable==True:
            if self.fullscreen==False:
                self.update_idletasks()
                self.overrideredirect(False)
                self.wm_state('zoomed')
                self.overrideredirect(True)
                self.after(10, lambda: self.set_appwindow())
                self.state('normal')
                self.fullscreen=True
                if self.style=="classic": self.button_max.configure(text="�'")
            else:
                self.geometry(f'+{self.x}+{self.y}')
                self.fullscreen=False
                if self.style=="classic": self.button_max.configure(text="□")
                
    def change_cursor(self, event):
        if (event.x in range(self.app.winfo_width()-10, self.app.winfo_width())
            and event.y in range(self.app.winfo_height()-10, self.app.winfo_height())):
            self.config(cursor="size_nw_se")
            return
        else:
            self.config(cursor="")
        
        if (event.x in range(self.app.winfo_width()-5, self.app.winfo_width())
            and event.y in range(0, self.app.winfo_height())):
            self.config(cursor="sb_h_double_arrow")
            return
        else:
            self.config(cursor="")

        if (event.x in range(0, self.app.winfo_width())
            and event.y in range(self.app.winfo_height()-5, self.app.winfo_height())):
            self.config(cursor="sb_v_double_arrow")
            return
        else:
            self.config(cursor="")
            
    def resize(self, event):
        if self.cget('cursor')=="size_nw_se":
            if event.x>100 and event.y>100:
                self.geometry(f"{event.x_root-self.x}x{event.y_root-self.y}")
        elif self.cget('cursor')=="sb_h_double_arrow":
            self.geometry(f"{event.x_root-self.x}x{self.winfo_height()}")
        elif self.cget('cursor')=="sb_v_double_arrow":
            self.geometry(f"{self.winfo_width()}x{event.y_root-self.y}")
            
    def configure(self, **kwargs):
        if "titlebar_color" in kwargs:
            self.titlebar_color = kwargs["titlebar_color"]
            self.header.configure(fg_color=self.titlebar_color)
        if "title" in kwargs:
            self.title_label.configure(text=f"  {kwargs['title']}")
        if "icon" in kwargs:
            self.icon = customtkinter.CTkImage(Image.open(kwargs["icon"]), size=(16,16))
            self.title_label.configure(image=self.icon)
        if "fg_color" in kwargs:
            self.app.configure(fg_color=fg_color)
        if "title_color" in kwargs:
            self.title_label.configure(text_color=kwargs['title_color'])     

if __name__=="__main__":    
    window = CTkWindow()
    # put widget in window.app 
    window.mainloop()