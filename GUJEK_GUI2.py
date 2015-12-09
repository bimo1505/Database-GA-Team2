from tkinter import *


##function if user choses 1 of the dropdown menu
def doThis():
    print('do')

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
dropdown.add_cascade(label = "Table", menu = subMenu)
subMenu.add_command(label="Analyst", command = doThis)
subMenu.add_command(label="Application", command = doThis)
subMenu.add_command(label="App Design Team", command = doThis)
subMenu.add_command(label="Customer", command = doThis)
subMenu.add_command(label="Delivery", command = doThis)
subMenu.add_command(label="Driver", command = doThis)
subMenu.add_command(label="Employee", command = doThis)
subMenu.add_command(label="Feedback", command = doThis)
subMenu.add_command(label="Food", command = doThis)
subMenu.add_command(label="Restaurant", command = doThis)
subMenu.add_command(label="Software Engineer", command = doThis)
subMenu.add_command(label="Supervisor", command = doThis)
subMenu.add_command(label="Taxi", command = doThis)
subMenu.add_command(label="Transaction", command = doThis)
subMenu.add_command(label="Vehicle", command = doThis)
subMenu.add_command(label="Works On", command = doThis)

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
