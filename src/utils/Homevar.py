import configparser
from src.utils.paths import homepageIni_directory

cg = configparser.ConfigParser()

cg.read(homepageIni_directory)
Main = 'Home_Main_Window'

bg = cg.get(Main, 'bg')
title = cg.get(Main, 'title')
width = cg.get(Main, 'width')
height = cg.get(Main, 'height')
frame_bg = cg.get(Main, 'framebg')
button_hover_bg = cg.get(Main, 'button_hover_bg')
text_color = cg.get(Main, 'text_color')
buttonOn_bg = cg.get(Main, 'buttonon_bg')