import sqlite3
import time

conn, c = "", ""


def connect_db():
    global conn, c
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    sql_create_table_info = '''CREATE TABLE IF NOT EXISTS VOTE_INFO (
        ID INTEGER PRIMARY KEY NOT NULL,
        FACTORY TEXT NOT NULL,
        UID TEXT,
        TIME TEXT 
    )'''
    sql_create_table_detail = '''CREATE TABLE IF NOT EXISTS VOTE_DETAIL(
        ID INTEGER PRIMARY KEY NOT NULL,
        UID TEXT,
        PRODUCT TEXT,
        CHOICE INTEGER,
        NOTE TEXT
    )'''
    c.execute(sql_create_table_info)
    c.execute(sql_create_table_detail)
    conn.commit()


def insert_db(item):
    global conn, c
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sql_insert_item = f'INSERT INTO FORM (NAME, OPTIONS, COMMENT, TIME) VALUES ("{item.name}", "{item.options}", ' \
                      f'"{item.comment}", "{now_time}")'
    try:
        c.execute(sql_insert_item)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True
