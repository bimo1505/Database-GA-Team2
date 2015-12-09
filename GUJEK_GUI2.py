from tkinter import *


##function if user choses 1 of the dropdown menu
def doThis():
    print('do')

def Exit():
    print('exit')

##window
root = Tk()

root.iconbitmap(default='gujeklogogui.ico')

##modify root window
root.title("Gujek Database")
root.geometry("300x400") #lengthXwidth
app = Frame(root)

label = Label(app, text = "Commands").pack(side=TOP, fill=BOTH)


"""Dropdown Menu"""
dropdown = Menu(root)
root.config(menu=dropdown)

subMenu = Menu(dropdown)
dropdown.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label="Table1", command = doThis)
subMenu.add_command(label="Table2", command = doThis)
subMenu.add_command(label="Table2", command = doThis)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = Exit)

editMenu = Menu(dropdown)
dropdown.add_cascade(label="edit", menu = editMenu)
editMenu.add_command(label="redo", command = doThis)

"""Command Buttons"""

showButton = Button(app, text = "Show Data").pack(side=TOP, fill=BOTH)
datapresent = Entry(app).pack(side=TOP, fill=BOTH)
createButton = Button(app, text = "Create").pack(side=TOP, fill=BOTH)
editButton = Button(app, text = "Edit").pack(side=TOP, fill=BOTH)
deleteButton = Button(app, text = "Delete").pack(side=TOP, fill=BOTH)

app.pack(fill=BOTH)
root.mainloop()
