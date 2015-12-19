import psycopg2
from psycopg2.extensions import adapt
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

conn = psycopg2.connect("dbname=asg_db user=postgres")
cursor = conn.cursor()

class Treeview(object):
    def __init__(self):
        self.root2 = Tk()
        self.tree = None
        self.dest = 'gujek.restaurant'
        self.tree_columns = self.get_column()
        self.tree_data = self.get_data()
        self._setup_widgets()
        self._build_tree()
        self.root2.mainloop()

    def _setup_widgets(self):
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6),
            text=("GUJEK Restaurant Table"))
        msg.pack(fill='x')

        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        # scrollbars for the treeview table
        self.tree = ttk.Treeview(columns=self.tree_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
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
            
treeview = Treeview()
cursor.close()
conn.close()
