from os import path, getcwd

project_directory = getcwd() # Project path

src_directory = path.join(path.join(project_directory), "src")# src folder path

utils_directory = path.join(path.join(src_directory), "utils")    # Utils folder path

assets_directory = path.join(path.join(src_directory), "assets")    # Assets folder path

app_directory = path.join(path.join(src_directory), "app")    # app folder

temps_directory = path.join(path.join(project_directory), "temps")    # temps folder

gen_lyrics_directory = path.join(path.join(temps_directory), "generated_lyrics") # Generated lyrics by whisper 

sliced_audio_directory = path.join(path.join(temps_directory), "sliced_audio") # Slicer audio by utils.slicer 

parameters_directory = path.join(path.join(project_directory), "parameters")  # data folder

homepageIni_directory = path.join(parameters_directory, "homepage.ini")    # setting.ini file path

fonts_directory = path.join((assets_directory), "fonts")     # fonts folder path


Opensans_font = path.join((fonts_directory), "OpenSans-Medium.ttf")
MonoLisa_font = path.join((fonts_directory), "MonoLisa-Bold.ttf")
