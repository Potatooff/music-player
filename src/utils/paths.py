from os import path, getcwd 

"""
Folder got underscore and start with lowercase"             ex: audio_slicer_directory = ... ( Folder )

This file may have somes mistakes, make sure it the good path by printing it to the console
"""


# // PROJECT PATH OVER HERE! //

    # Folders
project_directory = getcwd() # Project path

src_directory = path.join(path.join(project_directory), "src")          # src folder path

dataBackend_directory = path.join(path.join(project_directory), "data_backend")          # data_backend folder path

temps_directory = path.join(path.join(project_directory), "temps")      # temps folder path

settings_directory = path.join(path.join(project_directory), "settings")      # settings folder path

data_directory = path.join(path.join(project_directory), "data")          # data folder path

    # Files


# project/src

    # FOLDERS

src_engines_directory = path.join(path.join(src_directory), "engines")      # project/src/engine folder path

src_utils_directory = path.join(path.join(src_directory), "utils")          # project/src/utils folder path

src_ui_directory = path.join(path.join(src_directory), "ui")                # project/src/ui folder path

    # FILES


# project/src/engines

    # Folders

src_engines_LyricsGenerator_directory = path.join(path.join(src_engines_directory), "Lyrics_Generator") # Whisper Lyrics generator

    # Files

# project/src/engines/Lyrics_Generator

    # Folders

src_engines_LyricsGenerator_directory = path.join(path.join(src_engines_directory), "Lyrics_Generator") # Lyrics Generator path

    # Files

# project/src/ui

    # Folders
    
src_ui_auth_directory = path.join(path.join(src_ui_directory), "auth")        # project/src/ui/auth folder path

src_ui_error_directory = path.join(path.join(src_ui_directory), "error")        # project/src/ui/error folder path

    # Files

# project/src/ui/auth

    # Folders

    # Files

src_ui_auth_SignUp = path.join(path.join(src_ui_auth_directory), "sign_up.py")      # project/src/ui/auth/sign_up.py file path

# project/src/ui/error

    # Folders

    # Files

src_ui_error_ErrorPage = path.join(path.join(src_ui_error_directory), "error_page.py")      # project/src/ui/error/error_page.py file path


# project/data
    
    # Folders

data_songs_directory = path.join(path.join(data_directory), "songs")    # project/data/songs folder path

data_ui_directory = path.join(path.join(data_directory), "ui")          # project/data/ui folder path

    # Files



# project/data/songs

    # Folders

    # Files

data_songs_IAmWonder_directory = path.join(path.join(data_songs_directory), "I_am_wonder.mp3")


# project/data/ui

    # Folders

data_ui_fonts_directory = path.join(path.join(data_ui_directory), "fonts")      # project/data/ui/fonts folder path

data_ui_icons_directory = path.join(path.join(data_ui_directory), "icons")      # project/data/ui/icons folder path

data_ui_images_directory = path.join(path.join(data_ui_directory), "images")      # project/data/ui/images folder path


# projetct/data/ui/icon

    # Folders

    # Files

data_ui_icons_Logo_directory = path.join(path.join(data_ui_icons_directory), "logo.ico")        # MUSIC APP LOGO 64x64 PATH

data_ui_icons_LogoBigger_directory = path.join(path.join(data_ui_icons_directory), "logo_bigger.ico")       # MUSIC APP LOGO 512x512 PATH


# projetct/data/ui/fonts

    # Folders

    # Files

data_ui_fonts_JetBrainMono_directory = path.join(path.join(data_ui_fonts_directory), "JetBrainsMonoNL-Regular.ttf")


# project/settings

    # Folders

settings_ui_directory = path.join(path.join(settings_directory), "ui")      # project/settings/ui folder path

    # Files


# project/settings/ui

    # Folders

settings_ui_auth_directory = path.join(path.join(settings_ui_directory), "auth")      # project/settings/ui/auth folder path

    # Files


# project/settings/ui/auths

    # Folders

    # Files

settings_ui_auth_SignUpVar_directory = path.join(path.join(settings_ui_auth_directory), "sign_up_var.ini")      #  project/settings/ui/auth/sign_up_var.ini file path


# project/temps/lyrics

    # Folders
temps_lyrics_directory = path.join(path.join(temps_directory), "lyrics") 

    # Files

