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
        self.columns = []
        self.labels = dict()
        self._uWindow()
        self.root4.mainloop()

    def _uWindow(self):
        self.columns = self.get_columns()

        # generate entry form
        for i in range(len(self.columns)):
            Label(self.root4,
                  text="{}".format(self.columns[i])).grid(row=i, sticky=W)
            self.labels[self.columns[i]] = Entry(self.root4)
            self.labels[self.columns[i]].grid(row=i, column=1)

        u = Button(self.root3, text = "Update", command = self.yukganti)
        u.grid(columnspan=2, sticky=EW)

    def yukganti(self):
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

update = Update()
cursor.close()
conn.close()
