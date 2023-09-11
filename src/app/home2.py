from typing import Tuple
import customtkinter as c
from src.utils.Homevar import *
from src.utils.paths import Opensans_font, MonoLisa_font
from src.utils.image_engine import preprocess_icons
from time import sleep

# Preload settings
c.FontManager.load_font(Opensans_font)
c.FontManager.load_font(MonoLisa_font)

# -------- Somes variables --------------
search_text = "Type something here..."



# Loading icons <3
search_icon = preprocess_icons("search_icon.png", size=(32, 32))
exit_icon = preprocess_icons("exit_icon.png", size=(30, 30))
ExitSidebar_icon = preprocess_icons("ExitSidebar_icon.png", size=(30, 30))
ShowSidebar_icon = preprocess_icons("ShowSidebar_icon.png", size=(30, 30))
HomeSidebar_icon = preprocess_icons("home_icon.png", size=(30, 30))
Setting_icon = preprocess_icons("setting_icon.png", size=(28, 28))

# Loading fonts <3
Sidebar_font = "Open Sans Medium"
Lisa = "MonoLisa-Bold"

class homepage(c.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # Basic settings of class
        self.title(title)
        self.geometry(f"{width}x{height}")
        #self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1); self.grid_columnconfigure(0, weight=1)


        # Main frame also called main window woohoo
        self.main = c.CTkFrame(self, fg_color=bg)
        self.main.grid(row=0, column=0, padx=0 ,pady=0, sticky='nsew')

        # Grid manager sucks :c
        self.main.grid_columnconfigure((0, 1), weight=0)
        self.main.grid_columnconfigure((2, 3), weight=1)
        self.main.grid_rowconfigure((0, 1), weight=1)

        # Sidebar >>> Top bar

        self.sidebar = c.CTkFrame(self.main, fg_color=frame_bg)
        self.sidebar.grid(row=0, rowspan=2, column=0, padx=0, pady=0, sticky='ns')

        # Sidebar grid
        self.sidebar.grid_rowconfigure(0, weight=0)
        self.sidebar.grid_rowconfigure((1, 2, 3, 4, 5), weight=0)


        # Button to display Sidebar :3 
        self.show_sidebar = c.CTkButton(self.main, image=ShowSidebar_icon, text="", width=50,
                                        fg_color=bg, hover_color=frame_bg, command=self.ShowwSidebar)

        # // Sidebar Buttons //

        self.hide_sidebar = c.CTkButton(self.sidebar, image=ExitSidebar_icon, text="", fg_color="transparent", hover_color=button_hover_bg, width=50, command=self.HideSidebar)
        self.hide_sidebar.grid(row=0, column=0, padx=(80, 15), pady=(20, 20), sticky='ne')

        self.settings_button = c.CTkButton(self.sidebar, image=Setting_icon, fg_color="transparent", hover_color=button_hover_bg, width=70, height=50,
                                            text="Settings", font=(Sidebar_font, 20), text_color=text_color)
        self.settings_button.grid(row=3, column=0, padx=(14, 15), pady=20, sticky='ns')
    

        # Search button -> User is lost D:
        self.search__button = c.CTkButton(self.sidebar, image=search_icon, fg_color="transparent", hover_color=button_hover_bg, width=70, height=50,
                                           text="Search", font=(Sidebar_font, 20), text_color=text_color, command=self.searchbar_c)
        self.search__button.grid(row=2, column=0, padx=(10, 15), pady=(10, 20), sticky='ns')

        # Home button   -> There we go again
        self.home_button = c.CTkButton(self.sidebar, image=HomeSidebar_icon, fg_color="transparent", hover_color=button_hover_bg, width=70, height=50,
                                        text="Home", font=(Sidebar_font, 19), text_color=text_color, command=self.home_button_c)
        self.home_button.grid(row=1, column=0, padx=(10, 15), pady=20, sticky='ns')

        # // Search Section // -----------

        self.searchbar_frame = c.CTkFrame(self.main, fg_color=frame_bg)

        # Searchbar frame -> User no more lost or still ?
        self.searchbar_frame.grid_rowconfigure((0, 1), weight=0)
        self.searchbar_frame.grid_columnconfigure((0, 1), weight=1)

        # Search entry, what is user looking for?
        self.search_entry = c.CTkEntry(self.searchbar_frame, placeholder_text=search_text, corner_radius=10, height=55, font=(Lisa, 20))
        self.search_entry.grid(row=0, column=0, columnspan=2, padx=30, pady=30, sticky="nsew")

        
        


    # FUNCTIONS  -> Heehee

    def select_sidebar_frame(self, name) -> None:
        # set button color for selected button
        if name == "home":
            self.home_button.configure(fg_color=buttonOn_bg, text="")
            self.home_button.grid(row=1, column=0, padx=(0, 40), pady=20, sticky='ns')
        else:
            self.home_button.configure(fg_color="transparent", text="Home")
            self.home_button.grid(row=1, column=0, padx=(10, 15), pady=20, sticky='ns')

        if name == "search":
            self.search__button.configure(fg_color=buttonOn_bg, text="")
            self.search__button.grid(row=2, column=0, padx=(0, 40), pady=(10, 20), sticky='ns')
            self.searchbar_frame.grid(row=0, rowspan=2, column=1, columnspan=3, padx=20, pady=20, sticky="nsew")
        else:
            self.search__button.configure(fg_color="transparent", text="Search")
            self.search__button.grid(row=2, column=0, padx=(10, 15), pady=(10, 20), sticky='ns')
            self.searchbar_frame.grid_forget()

        if name == "settings":
            self.settings_button.configure(fg_color=buttonOn_bg, text="", width=70)
        else:
            self.settings_button.configure(fg_color="transparent")
        

    def HideSidebar(self) -> None:
        """Hide Sidebar"""
        self.sidebar.grid_forget()
        self.show_sidebar.grid(row=0, column=0, padx=0, pady=(200 ,15))
        print(self.search__button.winfo_width())
        print(self.search__button.winfo_height())
        
    

    def ShowwSidebar(self) -> None:
        """Pop up sidebar"""
        self.show_sidebar.grid_forget()
        self.sidebar.grid(row=0, rowspan=2, column=0, padx=0, pady=0, sticky='ns')
        

    def home_button_c(self) -> None:
        self.select_sidebar_frame("home")


    def searchbar_c(self) -> None:
        self.select_sidebar_frame("search")
        
    