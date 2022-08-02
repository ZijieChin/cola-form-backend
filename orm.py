import sqlite3
import time

conn, c = "", ""


def connect_db():
    global conn, c
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    sql_create_tables = '''CREATE TABLE IF NOT EXISTS FORM (
        ID INTEGER PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        OPTIONS TEXT,
        COMMENT TEXT,
        TIME TEXT 
    )'''
    c.execute(sql_create_tables)
    conn.commit()


def insert_db(item):
    global conn, c
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sql_insert_item = f'INSERT INTO FORM (NAME, OPTIONS, COMMENT, TIME) VALUES ("{item.name}", "{item.options}", ' \
                      f'"{item.comment}", "{now_time}")'
    print(sql_insert_item)
    try:
        c.execute(sql_insert_item)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True
