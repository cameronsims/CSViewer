import tkinter
from tkinter import ttk

import menu
import contextMenu
import fileParser
import cellHandler
import rowEdit
import programMeta

import os

# Create the window
window = tkinter.Tk()

style = ttk.Style()
style.theme_use('alt')

# Create important window things
window.title("CSViewer")
window.iconbitmap("./icons/csviewericon.ico")
window.geometry('512x512')
window.resizable(True, True)

# Tree where CSV values are shown
tree = ttk.Treeview(window)
tree["show"] = "headings"


xscroll = ttk.Scrollbar(window, 
                        orient = 'horizontal', 
                        command = tree.xview)
                        
yscroll = ttk.Scrollbar(window, 
                        orient = 'vertical', 
                        command = tree.yview)
                        
tree.config(xscrollcommand = xscroll.set)
tree.config(yscrollcommand = yscroll.set)

# Create context menu for tree
context_menu = tkinter.Menu(window, tearoff = 0)
contextMenu.create_contextMenu(context_menu)

# can't put this anywhere else
def open_contextMenu(event):
    contextMenu.open_contextMenu(context_menu, event.x_root, event.y_root)
    
tree.bind("<Button-3>", open_contextMenu)  # <Button-3> is right-click

meta = programMeta.program_meta("./examples/new.csv", ',')

menu.create_menubar(window, tree, meta)

# Add buttons
button_row = tkinter.Frame(window)

# ALIGN ON A GRID ##

tree.grid(row = 0, rowspan = 1, column = 0, columnspan = 1, sticky = "NSW")
xscroll.grid(row = 1, column = 0, sticky = "SWE")
yscroll.grid(row = 0, column = 1, sticky = "NSE")
button_row.grid(row = 2, column = 0, columnspan = 2, sticky="SWE")


rowEdit.create_row(button_row, tree)
            
window.columnconfigure(0, weight = 4)
window.columnconfigure(1, weight = 1)

window.rowconfigure(0, weight = 8)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)

window.mainloop()