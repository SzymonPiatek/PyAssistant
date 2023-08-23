from settings import *

import customtkinter as ctk

class VersionLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(
            master = parent, 
            text = text, 
            fg_color = COLOR, 
            justify = 'center', 
            text_color = TEXT_COLOR)
        
class FirstButton(ctk.CTkButton):
    def __init__(self, parent, text, func):
        super().__init__(
            master = parent, 
            fg_color = COLOR2, 
            text = text, 
            text_color = TEXT_COLOR2,
            command = func,
            corner_radius = 100)