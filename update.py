from tkinter import *
from psycopg2.extensions import adapt
import psycopg2

conn = psycopg2.connect("dbname=asg_db user=postgres")
cursor = conn.cursor()

class Update(object):
    def __init__(self):
        self.root4 = Tk()
        self.root4.resizable(0,0)
        self.root4.title("Update Entry")
        self.dest = 'gujek.restaurant'
        self.allCol = []
        self.allRow = []
        self.entries = dict()
        self._uWindow()
        self.root4.mainloop()

    def _uWindow(self):
        self.allCol = self.get_allCol()
        self.allRow = self.get_allRow()

        # list of options for dropdown menu
        first = []
        for i in range(len(self.allRow)):
            first.append(self.allRow[i][0])
            
        # dropdown menu
        lUpd = Label(self.root4, text = "Choose a Row to Update")
        try:
            self.chosen = StringVar(self.root4)
            self.chosen.set(first[0]) # default value
        except IndexError:
            self.root4.destroy()
            showerror("Index Error", "Table {} is empty".format(self.dest))
            raise Exception("Table {} is empty".format(self.dest))
        o = OptionMenu(self.root4, self.chosen, *first)
        ok = Button(self.root4, text="Next", command=self.next)
        lUpd.grid(columnspan=2, sticky=EW)
        o.grid(columnspan=2, sticky=EW)
        ok.grid(columnspan=2, sticky=EW)

    def next(self):
        # generate entry form
        for i in range(len(self.allRow)):
            if self.chosen.get() == self.allRow[i][0]:
                for j in range(len(self.allCol)):
                    Label(self.root4, text="{}".format(self.allCol[j])).grid(row=j+3, sticky=W)
                    self.entries[self.allCol[j]] = Entry(self.root4)
                    self.entries[self.allCol[j]].delete(0, END)
                    self.entries[self.allCol[j]].insert(0, self.allRow[i][j])
                    self.entries[self.allCol[j]].grid(row=j+3, column=1)
            else:
                continue
        u = Button(self.root4, text = "Update", command = self.yukganti)
        u.grid(row=len(self.allCol)+2, columnspan=2, sticky=EW)

    def yukganti(self):
        values = {k: str(adapt(v.get())) for k, v in self.entries.items()}
        final = ""
        for column in self.allCol:
            final += column + "=" + values.get(column) + ","
        cursor.execute("""UPDATE {}
                          SET {}
                          WHERE {}={};""".format(self.dest, final[:-1],
                                                 self.allCol[0],
                                                 values.get(self.allCol[0])))
        conn.commit()

    def get_allCol(self):
        # retrieve all names of the table's columns
        col = []
        cursor.execute("""SELECT attname
                          FROM   pg_attribute
                          WHERE  attrelid = {}::regclass
                          AND    attnum > 0
                          AND    NOT attisdropped
                          ORDER  BY attnum;""".format(str(adapt(self.dest))))
        fetched = cursor.fetchall()
        for i in range(len(fetched)):
            col.append(fetched[i][0])
        return col

    def get_allRow(self):
        # retrieve all rows from the table
        allRow = []
        cursor.execute("""SELECT *
                          FROM   {};""".format(self.dest))
        return cursor.fetchall()

update = Update()
cursor.close()
conn.close()
