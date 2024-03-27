import tkinter
import tkinter.font

import cellEditor

# The mutable cells    
class Row:
    def __init__(self, number, cells):
        self.number = number
        self.cells = cells
        self.cells.insert(0, self.number)
    
    def __str__(self):
        return str(self.number) + " " + str(self.cells)

def createCellHeader(tree, cells, row):
    columns = []
    columns = tree.heading(cells, text = cells, command = lambda:sort_column(tree, column, False))
    return columns
    
def createCell(tree, cells):
    cell = tree.insert("", tkinter.END, values = cells)
    return cell
    
def add_new_row(tree):
    child_amount = len(tree.get_children())
    cells = [ child_amount + 2 ]
    # For every number
    for n in range( len(tree["columns"]) - 1 ):
        cells.append("Enter Value")
    # Create a new row of cells
    createCell(tree, cells)
    # After the creation ask user to input new values
    cellEditor.edit_row(tree, child_amount + 1, cells)
    
def edit_row(tree, row):
    item = tree.item(row)
    values = item["values"]
    row_num = int(values[0]) -1
    cellEditor.edit_row(tree, row_num, row)

def delete_row(tree, row):
    tree.delete(row)
    # Change the row numbers
    i = 0
    for row_id in tree.get_children():
        # Get first element in values, and increase the '#' column
        item = tree.item(row_id)
        vals = item["values"]
        vals[0] = i + 1
        cellEditor.save_row(tree, i, vals)
        i = i + 1

def edit_col(tree):
    cellEditor.edit_columns(tree)

def sort_column(tree, column, reverse = False):
    cells = [(tree.set(child, column)) for child in tree.get_children()]