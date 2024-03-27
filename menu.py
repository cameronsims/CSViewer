import tkinter
import tkinter.messagebox

import fileParser

# Create menu bar
def create_menubar(window, tree, meta):
    # Create menu
    menu = tkinter.Menu(window)
    
    menu_file = create_filemenu(window, menu, tree, meta)
    menu_about = create_fileabout(window, menu)
    
    window.config(menu = menu)
    
def create_filemenu(window, menu, tree, meta):
    menu_file = tkinter.Menu(menu)
    
    # Create a new csv file
    menu_file.add_command(label = "New", command = None)
    
    # Save current file
    menu_file.add_command(label = "Save", command = lambda:fileParser.save(tree, meta, meta.delimeter))
    
    # Open an existing file
    menu_file.add_command(label = "Open", command = lambda:fileParser.open_new_file(tree, meta, meta.delimeter))
    
    # Add another file
    menu_file.add_command(label = "Concatenate File", command = lambda:fileParser.concat_new_file(tree, meta))
    
    # Keep file and exit away
    menu_file.add_separator()
    
    # Destroy window
    menu_file.add_command(label = "Exit", command = window.destroy)
    
    menu.add_cascade(label = "File", menu = menu_file)
    
    return menu_file
    
def create_fileabout(window, menu):
    menu_about = menu.add_command(label = "About", command = about)
    
    # Show pop-up window
    
    return menu_about

def about():
    abt = open("./examples/meta.csv", 'r')
    # 
    # data = abt.read().replace("\n", ", ").split(", ")
    # 
    # # Format the text
    # text = ""
    # length = int(len(data) / 2)
    # 
    # # Join the values
    # for i in range(length):
    #     text = text + data[i] + ": " + data[i + length] + '\n';
    
    # get lines
    data = abt.read().splitlines(True)
    
    # text that's going in the new box
    text = ""
    
    # skip first lines
    i = 0
    for row in data:
        if i != 0:
            cells = row.split(", ")
            text = text + cells[0] + ": " + cells[1]
        i = i + 1
    # Create a new box
    tkinter.messagebox.showinfo("About CSViewer", text)
    
    abt.close()