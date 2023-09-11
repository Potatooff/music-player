from PIL.Image import open
from customtkinter import CTkImage
from src.utils.paths import assets_directory
from os import path

def preprocess_icons(name: str, size):
    icon_path = path.join((assets_directory), name)
    img = open(icon_path)
    return CTkImage(img, size=size)
    

