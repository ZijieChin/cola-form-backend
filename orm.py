import sqlite3
import time
import uuid

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
    uid = str(uuid.uuid1())
    sql_insert_info = f"INSERT INTO VOTE_INFO (FACTORY, UID, TIME) VALUES ('{item.factory}', '{uid}', '{now_time}')"
    choices = []
    for choice in item.choices:
        choices.append((uid, choice.value, choice.chosen, choice.note))
    sql_insert_detail = f"INSERT INTO VOTE_DETAIL (UID, PRODUCT, CHOICE, NOTE) VALUES (?, ?, ?, ?)"
    try:
        c.execute(sql_insert_info)
        c.executemany(sql_insert_detail, choices)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True

def query_db():
    global conn, c
    sql_query_all_uids = "SELECT DISTINCT UID FROM VOTE_INFO"
    c.execute(sql_query_all_uids)
    uids = c.fetchall()
    sql_query_all_products = "SELECT DISTINCT PRODUCT FROM VOTE_DETAIL ORDER BY PRODUCT"
    c.execute(sql_query_all_products)
    products = c.fetchall()
    for uid in uids:
        sql_query_info = f"SELECT * FROM VOTE_INFO WHERE UID = '{uid[0]}'"
        sql_query_detail = f"SELECT * FROM VOTE_DETAIL WHERE UID = '{uid[0]}'"
        c.execute(sql_query_info)
        infos = c.fetchall()
        c.execute(sql_query_detail)
        details = c.fetchall()
