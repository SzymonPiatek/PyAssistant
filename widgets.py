from settings import *

import customtkinter as ctk

class VersionLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(
            master = parent, 
            text = text, 
            fg_color = COLOR, 
            justify = 'center', 
            text_color = TEXT_COLOR,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE, weight = 'bold')))
        
class FirstLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(
            master = parent, 
            fg_color = COLOR, 
            text = text, 
            text_color = COLOR2, 
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE3, weight = 'bold')))
        
class FirstButton(ctk.CTkButton):
    def __init__(self, parent, text, func):
        super().__init__(
            master = parent, 
            fg_color = COLOR2, 
            text = text, 
            text_color = TEXT_COLOR2,
            command = func,
            corner_radius = 100,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE2, weight = 'bold')))