def error_window(the_error: str) -> None:
    the_error = f"An unexpected error occurred: {the_error}"
    the_error = resize_text(the_error)
    import dearpygui.dearpygui as dpg
    from src.utils.paths import  data_ui_icons_Logo_directory as logo
    from src.utils.paths import   data_ui_icons_LogoBigger_directory as logo_bigger

    dpg.create_context()

    # Create a window
    with dpg.window(tag="ERROR - PAGE 404"):
        dpg.add_text(the_error)

    dpg.create_viewport(title='ERROR - PAGE 404', width=400, height=200, small_icon=logo, large_icon=logo_bigger, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("ERROR - PAGE 404", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def resize_text(text: str) -> str:
    """This makes a new line after 50 characters to not break ui"""
    max_line_length: int = 50
    result = ""
    for i in range(0, len(text), max_line_length):
        result += text[i:i+max_line_length] + "\n"
    return result
