import sqlite3


def create_table(sql_file):
    with open (sql_file, "r") as f:             
        sql=f.read()                    #Читаємо sql команду
    with sqlite3.connect("task.db") as con:             #Створємо файл за sql
        cur=con.cursor()
        cur.executescript(sql)

if __name__=="__main__":
    create_table("tables.sql")