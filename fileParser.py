import tkinter
import tkinter.filedialog
from tkinter import ttk

import programMeta
import cellHandler

def open_new_file(tree, meta, delimeter = ','):
    # Clear any data in a tree
    tree.delete( * tree.get_children() )
    # Get new file
    file_name = tkinter.filedialog.askopenfilename()
    meta.changeFileName(file_name)
    # Add info
    add(tree, file_name, delimeter)
   
def concat_new_file(tree, file_name, delimeter = ','):
     # Get new file
    new_file_name = tkinter.filedialog.askopenfilename()
    # Add info
    add(tree, new_file_name, delimeter)
    
def add(tree, file_name, delimeter = ','):
    # Open the file
    file = ''
    try:
        file = open(file_name)
        # Add new data
        parse(file, tree, delimeter)
        # Make file line smaller
        tree.column('#', minwidth = 10, width = 20, stretch = Yes)
        # Close the file
        file.close()
    except:
        print("No file selected!")
        
def parse(file, tree, delimeter = ','):
    # Go To Start of File
    file.seek(0)
    # For every row: make it an item
    i = 1   # Row
    j = 0   # Column
    for row in file:
        # Create cell
        r = cellHandler.Row(i, row.replace('\n', '').replace(str(delimeter) + ' ', delimeter).split(delimeter))
        # When i=0, we will be inputting headers
        if i == 1:
            r.cells[0] = '#'
            tree["columns"] = r.cells
            # Add header
            for cell in r.cells:
                cellHandler.createCellHeader(tree, cell, j + 1)
                tree.column(cell, stretch=tkinter.YES)
                j = j + 1
        else:
            # If we are not on the first row, create a cell
            cellHandler.createCell(tree, r.cells)
            
        i = i + 1
        
def save(tree, file_name, delimeter = ','):
    def save_row(row):
        n = len(row)
        # for every item in the row
        for i in range(n):
            # if not the first element
            if i != 0: 
                # Write in file
                file.write(str(row[i]))
                # If it isn't a row
                if i != (n-1):
                    file.write(str(delimeter) + " ")
        file.write('\n')
    # Open file
    file = open(file_name.file_name, "w")
    # Add column headers
    row = tree["column"]
    row_text = []
    for item in row:
        row_text.append(tree.heading(item)["text"])
    save_row(row_text)
    # Add values
    for child in tree.get_children():
        # save the proper values
        row = tree.item(child)["values"]
        save_row(row)  
    
    # CLose file
    file.close()