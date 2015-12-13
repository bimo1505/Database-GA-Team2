from tkinter import *
import psycopg2

conn = psycopg2.connect("dbname=asg_db user=postgres")
cursor = conn.cursor()

class Delete(object):
    def __init__(self):
        self.root5 = Tk()
        self.dest = 'gujek.customer'
        self.pKey = None
        self.options = []
        self.chosen = None
        self._doItBitch()
        self.root5.mainloop()

    def _doItBitch(self):
        self.pKey = self.get_first()
        self.options = self.get_options()

        self.root5.title("Delete Entry")
        self.root5.geometry("300x100")

        lDel = Label(self.root5, text = "Choose a Row to Delete")
        self.chosen = StringVar(self.root5)
        self.chosen.set(self.options[0]) # default value
        w = OptionMenu(self.root5, self.chosen, *self.options)
        x = Button(self.root5, text = "Delete", command = self.yukhapus)
        
        lDel.pack(side=TOP, fill=BOTH)
        w.pack(side=TOP, fill=BOTH)
        x.pack(side=TOP, fill=BOTH)

    def yukhapus(self):
        cursor.execute("""DELETE FROM {}
                          WHERE {}='{}';"""\
                       .format(self.dest, self.pKey, self.chosen.get()))
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
        # retrieve all values from the table's first column
        opt = []
        cursor.execute("""SELECT {}
                          FROM   {};""".format(self.pKey, self.dest))
        fetched = cursor.fetchall()
        for i in range(len(fetched)):
            opt.append(fetched[i][0])
        return opt

delete = Delete()
cursor.close()
conn.close()
