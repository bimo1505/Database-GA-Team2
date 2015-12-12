import psycopg2
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

# initialize connection to Gujek Database
conn = psycopg2.connect("dbname=ASG_DB user=postgres")
cursor = conn.cursor()

""" -------------------------MAIN WINDOW------------------------- """
# root window
root = Tk()
root.title("Gujek Database")
root.geometry("300x400") # width x length
app = Frame(root)

"""Dropdown Menu"""
dropdown = Menu(root)
root.config(menu=dropdown)

subMenu = Menu(dropdown)
dropdown.add_cascade(label="Table", menu = subMenu)
subMenu.add_command(label="Analyst",
                    command = lambda: doThis("analyst"))
subMenu.add_command(label="Application",
                    command = lambda: doThis("app"))
subMenu.add_command(label="App Design Team",
                    command = lambda: doThis("app_design_team"))
subMenu.add_command(label="Customer",
                    command = lambda: doThis("customer"))
subMenu.add_command(label="Delivery",
                    command = lambda: doThis("delivery"))
subMenu.add_command(label="Driver",
                    command = lambda: doThis("driver"))
subMenu.add_command(label="Employee",
                    command = lambda: doThis("employee"))
subMenu.add_command(label="Feedback",
                    command = lambda: doThis("feedback"))
subMenu.add_command(label="Food",
                    command = lambda: doThis("food"))
subMenu.add_command(label="Restaurant",
                    command = lambda: doThis("restaurant"))
subMenu.add_command(label="Software Engineer",
                    command = lambda: doThis("software_engineer"))
subMenu.add_command(label="Supervisor",
                    command = lambda: doThis("supervisor"))
subMenu.add_command(label="Taxi",
                    command = lambda: doThis("taxi"))
subMenu.add_command(label="Transaction",
                    command = lambda: doThis("transaction"))
subMenu.add_command(label="Vehicle",
                    command = lambda: doThis("vehicle"))
subMenu.add_command(label="Works On",
                    command = lambda: doThis("works_on"))

# displays table address as used for SQL query
# in the datapresent text box
dest = ""
def doThis(table=str):
    global dest
    dest = "gujek.{}".format(table)
    datapresent.configure(state="normal")
    datapresent.delete(0, END)
    datapresent.insert(0, dest)
    datapresent.configure(state="disabled")

"""Command Buttons"""
l1 = Label(app, text = "Choose a Table")
datapresent = Entry(app)
datapresent.configure(state="disabled")
l2 = Label(app, text = "Choose an Operation")

""" -------------------------SHOW WINDOW------------------------- """

tree_columns = []
tree_data = []

class Treeview(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        self.Child_Window()
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6),
            text=("GUJEK Restaurant Table"))
        msg.pack(fill='x')

        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        # scrollbars for the treeview table
        self.tree = ttk.Treeview(columns=tree_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # XXX tkFont.Font().measure expected args are incorrect according
            #     to the Tk docs
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in tree_data:
            self.tree.insert('', 'end', values=item)

            # adjust columns lenghts if necessary
            for indx, val in enumerate(item):
                ilen = tkFont.Font().measure(val)
                if self.tree.column(tree_columns[indx], width=None) < ilen:
                    self.tree.column(tree_columns[indx], width=ilen)

    def sortby(tree, col, descending):
        """Sort tree contents when a column is clicked on."""
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]

        # reorder data
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

        # switch the heading so that it will sort in the opposite direction
        tree.heading(col,
                     command=lambda col=col: sortby(tree, col, int(not descending)))
                    
    def Child_Window(self):
        win2 = Toplevel()
        treeScroll = ttk.Scrollbar(win2)
        treeScroll.pack(side=RIGHT, fill=Y)
        tree = ttk.Treeview(win2,columns=tree_columns, show="headings")
        tree.pack(side=LEFT, fill=BOTH)
                    
def fartbag():
    global tree_columns, tree_data
    cursor.execute("""SELECT attname
                   FROM   pg_attribute
                   WHERE  attrelid = '{}'::regclass
                   AND    attnum > 0
                   AND    NOT attisdropped
                   ORDER  BY attnum;""".format(dest))
    fetched = cursor.fetchall()
    for i in range(len(fetched)):
        tree_columns.append(fetched[i][0])

    cursor.execute("""SELECT * FROM {}""".format(dest))
    for entry in cursor.fetchall():
        tree_data.append(entry)

    treeview = Treeview()

""" ----------------------END OF SHOW WINDOW--------------------- """

showButton = Button(app, text = "Show Table", command = fartbag)
createButton = Button(app, text = "Create Entry")
editButton = Button(app, text = "Update Entry")

""" ------------------------DELETE WINDOW------------------------ """

def delete():
    cursor.execute("""DELETE FROM {}
                   WHERE CustomerName='Alfreds Futterkiste' AND ContactName='Maria Anders';""".format(dest()))

def bag():
    # retrieve the table's name of primary key column
    cursor.execute("""SELECT a.attname
                   FROM   pg_index i
                   JOIN   pg_attribute a ON a.attrelid = i.indrelid
                                         AND a.attnum = ANY(i.indkey)
                   WHERE  i.indrelid = '{}'::regclass
                   AND    i.indisprimary;""".format(dest))
    pkey = cursor.fetchone()[0]

    # retrieve all values from the table's primary key column
    cursor.execute("""SELECT {}
                   FROM   {};""".format(pkey, dest))

    OPTIONS = []
    fetched = cursor.fetchall()
    for i in range(len(fetched)):
        OPTIONS.append(fetched[i][0])

    root5 = Tk()
    root5.title("Delete Entry")
    root5.geometry("300x100")

    lDel = Label(root5, text = "Choose a Row to Delete")
    variable = StringVar(root5)
    variable.set(OPTIONS[0]) # default value

    w = OptionMenu(root5, variable, *OPTIONS)
    deleteBtn = Button(root5, text = "Delete")
    
    lDel.pack(side=TOP, fill=BOTH)
    w.pack(side=TOP, fill=BOTH)
    deleteBtn.pack(side=TOP, fill=BOTH)

    mainloop()

""" ---------------------END OF DELETE WINDOW-------------------- """

deleteButton = Button(app, text = "Delete Entry", command = bag)

l1.pack(side=TOP, fill=BOTH)
datapresent.pack(side=TOP, fill=BOTH)
l2.pack(side=TOP, fill=BOTH)
showButton.pack(side=TOP, fill=BOTH)
createButton.pack(side=TOP, fill=BOTH)
editButton.pack(side=TOP, fill=BOTH)
deleteButton.pack(side=TOP, fill=BOTH)

app.pack(fill=BOTH)
root.mainloop()

cursor.close()
conn.close()
