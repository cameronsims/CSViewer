import tkinter

import cellHandler
import fileParser

def create_row(panel, tree):
    # Add a button
    add_row = tkinter.Button(panel, text = "New Row", command = lambda:cellHandler.add_new_row(tree))
    add_row.grid(row = 0, column = 0)
    
    edit_row = tkinter.Button(panel, text = "Edit Row", command = lambda:cellHandler.edit_row(tree, tree.focus()))
    edit_row.grid(row = 0, column = 1)
    
    delete_row = tkinter.Button(panel, text = "Delete Row", command = lambda:cellHandler.delete_row(tree, tree.focus()))
    delete_row.grid(row = 0, column = 2)
    
    add_col = tkinter.Button(panel, text = "New Column")
    add_col.grid(row = 1, column = 0)
    
    edit_col = tkinter.Button(panel, text = "Edit Column", command = lambda:cellHandler.edit_col(tree))
    edit_col.grid(row = 1, column = 1)
    
    delete_col = tkinter.Button(panel, text = "Delete Column")
    delete_col.grid(row = 1, column = 2)
    
    #save_file = tkinter.Button(window, text = "Save", command = lambda:fileParser.save(tree, meta.file_name))
    #save_file.grid(row = 2, column = 0)
    
    panel.columnconfigure(0, weight = 1)
    panel.columnconfigure(1, weight = 1)
    panel.columnconfigure(2, weight = 1)
    
    panel.rowconfigure(0, weight = 1)
    panel.rowconfigure(1, weight = 1)