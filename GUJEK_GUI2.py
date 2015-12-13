import psycopg2
from psycopg2.extensions import adapt

from tkinter import ttk
from tkinter import *

from tkinter.messagebox import showerror
import tkinter.font as tkFont

# initialize connection to Gujek Database
conn = psycopg2.connect("dbname=asg_db user=postgres")
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

class Treeview(object):
    def __init__(self):
        self.root2 = Tk()
        self.root2.title("Show Table")
        self.tree = None
        self.dest = dest
        self.tree_columns = self.get_column()
        self.tree_data = self.get_data()
        self._setup_widgets()
        self._build_tree()
        self.root2.mainloop()

    def _setup_widgets(self):
        msg = ttk.Label(self.root2, wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6),
            text=("{}".format(self.dest)))
        msg.pack(fill='x')

        container = ttk.Frame(self.root2)
        container.pack(fill='both', expand=True)

        # scrollbars for the treeview table
        self.tree = ttk.Treeview(container, columns=self.tree_columns, show="headings")
        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: self.sortby(c, 0))
            # XXX tkFont.Font().measure expected args are incorrect according
            #     to the Tk docs
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in self.tree_data:
            self.tree.insert('', 'end', values=item)

            # adjust columns lenghts if necessary
            for indx, val in enumerate(item):
                ilen = tkFont.Font().measure(val)
                if self.tree.column(self.tree_columns[indx], width=None) < ilen:
                    self.tree.column(self.tree_columns[indx], width=ilen)

    def sortby(self, col, descending):
        """Sort tree contents when a column is clicked on."""
        # grab values to sort
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)

        # switch the heading so that it will sort in the opposite direction
        self.tree.heading(col,
                     command=lambda col=col: self.sortby(col, int(not descending)))

    def get_column(self):
        # retrieve column names in the table
        fetch = []
        cursor.execute("""SELECT attname
                          FROM   pg_attribute
                          WHERE  attrelid = '{}'::regclass
                          AND    attnum > 0
                          AND    NOT attisdropped
                          ORDER  BY attnum;""".format(self.dest))
        fetched = cursor.fetchall()
        for i in range(len(fetched)):
            fetch.append(fetched[i][0])
        return fetch

    def get_data(self):
        # retrieve all rows in the table
        retch = []
        cursor.execute("""SELECT * FROM {}""".format(self.dest))
        for entry in cursor.fetchall():
            retch.append(entry)
        return retch

""" ----------------------END OF SHOW WINDOW--------------------- """

showButton = Button(app, text = "Show Table", command = Treeview)

""" ------------------------CREATE WINDOW------------------------ """

class Create(object):
    def __init__(self):
        self.root3 = Tk()
        self.root3.resizable(0,0)
        self.root3.title("Create Entry")
        self.dest = dest
        self.columns = []
        self.labels = dict()
        self._cWindow()
        self.root3.mainloop()

    def _cWindow(self):
        self.columns = self.get_columns()

        # generate entry form
        for i in range(len(self.columns)):
            Label(self.root3,
                  text="{}".format(self.columns[i])).grid(row=i, sticky=W)
            self.labels[self.columns[i]] = Entry(self.root3)
            self.labels[self.columns[i]].grid(row=i, column=1)

        c = Button(self.root3, text = "Create", command = self.yukbikin)
        c.grid(columnspan=2, sticky=EW)

    def yukbikin(self):
        values = {k: str(adapt(v.get())) for k, v in self.labels.items()}
        final = ""
        for column in self.columns:
            final += values.get(column) + ","
        cursor.execute("""INSERT INTO {}
                          VALUES ({});""".format(self.dest, final[:-1]))
        conn.commit()

    def get_columns(self):
        # retrieve all columns from the table
        col = []
        cursor.execute("""SELECT attname
                          FROM   pg_attribute
                          WHERE  attrelid = '{}'::regclass
                          AND    attnum > 0
                          AND    NOT attisdropped
                          ORDER  BY attnum;""".format(self.dest))
        fetched = cursor.fetchall()
        for i in range(len(fetched)):
            col.append(fetched[i][0])
        return col
    
""" ---------------------END OF CREATE WINDOW-------------------- """
    
createButton = Button(app, text = "Create Entry", command = Create)
editButton = Button(app, text = "Update Entry")

""" ------------------------DELETE WINDOW------------------------ """

class Delete(object):
    def __init__(self):
        self.root5 = Tk()
        self.root5.title("Delete Entry")
        self.root5.geometry("180x80")
        self.dest = dest
        self.first = None
        self.options = []
        self.chosen = None
        self._dWindow()
        self.root5.mainloop()

    def _dWindow(self):
        self.first = self.get_first()
        self.options = self.get_options()

        lDel = Label(self.root5, text = "Choose a Row to Delete")
        try:
            self.chosen = StringVar(self.root5)
            self.chosen.set(self.options[0]) # default value
        except IndexError:
            self.root5.destroy()
            showerror("Index Error", "Table {} is empty".format(self.dest))
            raise Exception("Table {} is empty".format(self.dest))
        w = OptionMenu(self.root5, self.chosen, *self.options)
        d = Button(self.root5, text = "Delete", command = self.yukhapus)
        
        lDel.pack(side=TOP, fill=BOTH)
        w.pack(side=TOP, fill=BOTH)
        d.pack(side=TOP, fill=BOTH)

    def yukhapus(self):
        cursor.execute("""DELETE FROM {}
                          WHERE {}={};"""\
                       .format(self.dest, self.first,
                               str(adapt(self.chosen.get()))))
        conn.commit()

    def get_first(self):
        # retrieve the name of the table's first column
        cursor.execute("""SELECT attname
                          FROM   pg_attribute
                          WHERE  attrelid = '{}'::regclass
                          AND    attnum > 0
                          AND    NOT attisdropped
                          ORDER  BY attnum;""".format(self.dest))
        return cursor.fetchone()[0]

    def get_options(self):
        # retrieve all values from the table's primary key column
        opt = []
        cursor.execute("""SELECT {}
                          FROM   {};""".format(self.first, self.dest))
        fetched = cursor.fetchall()
        for i in range(len(fetched)):
            opt.append(fetched[i][0])
        return opt

""" ---------------------END OF DELETE WINDOW-------------------- """

deleteButton = Button(app, text = "Delete Entry", command = Delete)

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
