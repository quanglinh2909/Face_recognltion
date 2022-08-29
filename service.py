import sqlite3

def getData():
    conn = sqlite3.connect('data/data.db')
    cursor = conn.execute("SELECT * FROM Addict")
    data = cursor.fetchall()
    print(data)
    conn.close()

def insert():
    conn = sqlite3.connect('data/data.db')
    sql =  """
    INSERT INTO Addict(name,data,idAddict) values (?,?)
     """
    cur = conn.cursor()
    data = conn.execute(sql,("name","data"))
    conn.commit()
    conn.close()
    return  cur.lastrowid
print(insert())
getData()
