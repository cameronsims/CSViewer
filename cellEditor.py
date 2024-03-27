import tkinter
import tkinter.messagebox

def edit_panel(popup_menu, tree, row, columns, text_inputs, lambda_ok):
    popup_menu.columnconfigure(0, weight = 1)
    popup_menu.columnconfigure(1, weight = 5)
    
    # for every single cell the row has:
    i = 0
    for cell in columns:
        print(cell)
        # ignore the page number
        if i != 0:
            label = tkinter.Label(popup_menu, text=columns[i])
            label.grid(column = 0, row = i - 1)
            
            # create a submission box
            text = tkinter.Text(popup_menu, width = 16, height = 1)
            text.insert(tkinter.END, row[i])
            text.grid(column = 1, row = i - 1)
            
            text_inputs.append(text)
            
            popup_menu.rowconfigure(i, weight = 2)
            
        # increment
        i = i + 1
    # Create Submission/Decline Button
    btn = tkinter.Button(popup_menu, text="Ok", command = lambda_ok)
    btn.grid(column = 0, row = i)
    
    btn = tkinter.Button(popup_menu, text="Cancel", command = popup_menu.destroy)
    btn.grid(column = 1, row = i)
    
    popup_menu.rowconfigure(i, weight = 1)

def edit_row(tree, id, row):
    # Create pop-up menu
    popup_menu = tkinter.Tk()
    # get colums
    columns = tree["columns"]
    # the values that we are going to change
    text_inputs = []
    
    edit_panel(popup_menu, tree, row, columns, text_inputs, lambda:save_values_to_row(popup_menu, tree, text_inputs, id, row))

def save_values_to_row(window, tree, inputs, id, row):
    row = get_values(inputs)
    # add row number to the end
    row.insert(0, id + 1)
    save_row(tree, id, row)
    
    window.destroy()

def get_values(inputs):
    cells = []
    i = 0
    for input in inputs:
        text = input.get("1.0", tkinter.END)
        # remove \n character
        if len(text) > 1:
            text = text[:-1]
        # add to the cells
        cells.append(text)
    return cells

def save_row(tree, id, row):
    item_ids = tree.get_children()
    item = tree.item(item_ids[id - 1], values = tuple(row))
    
def save_cell(tree, id, row):
    # Save new data
    tree.insert("", tkinter.END, text=row[i])

def save_values_to_col(popup_menu, tree, inputs):
    # new column names
    new_cols = get_values(inputs)
    old_cols = tree["columns"]
    print(old_cols)
    print(new_cols)
    # for every text input, change value
    i = 0
    for column in inputs:
        tree.heading(old_cols[i + 1], text = new_cols[i])
        i = i + 1
    # kill the window
    popup_menu.destroy()

def edit_columns(tree):
    # Create pop-up menu
    popup_menu = tkinter.Tk()
    # get colums to rename
    columns = tree["columns"]
    # new names for columns
    text_inputs = []
    
    edit_panel(popup_menu, tree, list(columns), columns, text_inputs, lambda:save_values_to_col(popup_menu, tree, text_inputs)) #, id, row))