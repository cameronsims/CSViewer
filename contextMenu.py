def create_contextMenu(context_menu):
    context_menu.add_command(label = "Name")

def open_contextMenu(context_menu, x, y):
    try:
        context_menu.tk_popup(x, y)
    finally:
        context_menu.grab_release()