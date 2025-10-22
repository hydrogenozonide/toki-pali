import dearpygui.dearpygui as dpg
import webbrowser

def open_window(window):
    dpg.show_item(window)

def toggle_fullscreen():
    dpg.toggle_viewport_fullscreen()

dpg.create_context()
dpg.configure_app(docking = True, docking_space = True)
dpg.create_viewport(title = 'toki pali Alpha 0.0.1', width = 800, height = 600)

dpg.set_viewport_small_icon("pali.ico")
dpg.set_viewport_large_icon("pali.ico")

dpg.add_file_dialog(directory_selector = True, show = False, tag = "project_open", width = 700, height = 400)

with dpg.viewport_menu_bar():
    with dpg.menu(label = "Project"):
        dpg.add_menu_item(label = "New")
        dpg.add_menu_item(label = "Open", callback = lambda: dpg.show_item("project_open"))
        dpg.add_menu_item(label = "Save")
        dpg.add_menu_item(label = "Save as")
        
    with dpg.menu(label = "Window"):
        with dpg.menu(label = "Open"):
            with dpg.menu(label = "Tools"):
                dpg.add_menu_item(label = "Welcome", callback = lambda: open_window("welcome"))
                dpg.add_menu_item(label = "Metrics", callback = lambda: dpg.show_tool(dpg.mvTool_Metrics))
                dpg.add_menu_item(label = "Documentation", callback = lambda: webbrowser.open("https://github.com/hydrogenozonide/toki-pali/wiki"))
            dpg.add_menu_item(label = "Test window", callback = lambda: open_window("test_window"))
            
        with dpg.menu(label = "Style"):
            dpg.add_checkbox(label="Fullscreen", callback = toggle_fullscreen)
        
    with dpg.menu(label = "Lexicon"):
        dpg.add_menu_item(label = "item", callback = lambda: open_window("test_window"))
        
    with dpg.menu(label = "Phonology"):
        dpg.add_menu_item(label = "item", callback = lambda: open_window("test_window"))

    with dpg.menu(label = "Plugins"):
        dpg.add_menu_item(label = "Manage plugins")

with dpg.window(label = "test window", tag = "test_window", show = False):
    dpg.add_text("text")
    dpg.add_button(label = "button")
    dpg.add_input_text(label = "string", default_value = "default text")
    dpg.add_slider_float(label = "float", default_value = 0, max_value = 1)
    dpg.add_slider_int(label = "int", default_value = 0, max_value = 100)


with dpg.window(label = "Welcome", tag = "welcome", width=275, height=75):
    dpg.add_text("Welcome to Alpha 0.0.1 of toki pali!")
    dpg.add_button(label = "New project")
    dpg.add_same_line()
    dpg.add_button(label = "Open existing project", callback = lambda: dpg.show_item("project_open"))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
