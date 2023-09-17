from configparser import ConfigParser
from src.utils.paths import settings_ui_auth_SignUpVar_directory
from src.ui.error.error_page import error_window

config = ConfigParser() # config is now an object

config.read(settings_ui_auth_SignUpVar_directory)   # This will read the .ini file from that variable path


UI_SECTION = "ui"   # Section name
value = config.get(UI_SECTION, 'MainWindow_width')  # variable wanted use .set instead of .get to change the value




def save_ini_file(paths) -> None:
    """This will save any change made to the .ini file return None """
    # config.set('Section1', 'key1', 'new_value')   # Use this if you want to change value
    try:
        with open(paths, 'w') as configfile:
            config.write(configfile)
    except:
        error_window("Error writing file!")


