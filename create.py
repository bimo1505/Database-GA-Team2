from tkinter import *
from psycopg2.extensions import adapt
import psycopg2

conn = psycopg2.connect("dbname=asg_db user=postgres")
cursor = conn.cursor()

class Create(object):
    def __init__(self):
        self.root3 = Tk()
        self.root3.resizable(0,0)
        self.root3.title("Create Entry")
        self.dest = 'gujek.restaurant'
        self.columns = []
        self.labels = dict()
        self._doItBitch()
        self.root3.mainloop()

    def _doItBitch(self):
        self.columns = self.get_columns()

        # generate entry form
        for i in range(len(self.columns)):
            Label(self.root3,
                  text="{}".format(self.columns[i])).grid(row=i, sticky=W)
            self.labels[self.columns[i]] = Entry(self.root3)
            self.labels[self.columns[i]].grid(row=i, column=1)

        c = Button(self.root3, text = "Create Entry", command = self.yukbikin)
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

create = Create()
cursor.close()
conn.close()
