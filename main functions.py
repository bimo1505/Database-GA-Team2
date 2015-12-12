import psycopg2

conn = psycopg2.connect("dbname=ASG_DB user=postgres")
cursor = conn.cursor()

# retrieves table attribute that is a primary key
def get_pKey():
    cursor.execute("""SELECT a.attname
                   FROM   pg_index i
                   JOIN   pg_attribute a ON a.attrelid = i.indrelid
                                         AND a.attnum = ANY(i.indkey)
                   WHERE  i.indrelid = 'gujek.restaurant'::regclass
                   AND    i.indisprimary;""")
    return cursor.fetchone()[0]

# prints out all entries in a table
def viewTable():
    cursor.execute("""SELECT * FROM gujek.restaurant""")
    for entry in cursor.fetchall():
        print(entry)

# inserts a new entry into a table
def insertEntry():
    cursor.execute("""INSERT INTO gujek.restaurant
                   VALUES ('Starbucks Coffee', 'Pumpkin Spice Latte', '50000', 'Cilandak Town Square', '0217505943');""")
    conn.commit()

# updates an existing entry in a table
def updateEntry():
    cursor.execute("""UPDATE gujek.restaurant
                   SET price='15000'
                   WHERE {}='Wingstop'""".format(get_pKey()))
    conn.commit()

# deletes an existing entry from a table
def deleteEntry():
    cursor.execute("""DELETE FROM gujek.restaurant
                   WHERE {}='Wingstop'""".format(get_pKey()))
    conn.commit()

cursor.close()
conn.close()
