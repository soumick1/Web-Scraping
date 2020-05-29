import sqlite3


def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS GRAPHICS_CARDS (NAME TEXT, PRICE TEXT, SHIPPING TEXT, RATING TEXT, NUMBER_OF_REVIEWS TEXT)")
    conn.close()


def insert_info_table(dbname, values):
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT INTO GRAPHICS_CARDS (NAME, PRICE, SHIPPING, RATING, NUMBER_OF_REVIEWS) VALUES (?, ?, ?, ?, ?)",
                 values)
    conn.commit()
    conn.close()


def get_graphics_card_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    table_data = cur.fetchall()

    for record in table_data:
        print(record)
    conn.close()
