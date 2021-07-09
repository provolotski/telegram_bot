import sqlite3
from sqlite3 import Error


def get_connect():
    try:
        connection = sqlite3.connect('tg_bot.db')
        return connection
    except Error:
        print(Error)


def generate_scheme():
    pass


def getUserId(tg_user_id):
    conn = get_connect()
    cursor = conn.cursor()
    rows = cursor.execute("select id from users where tg_id = ?", (str(tg_user_id),))
    res = 0
    for row in rows:
        print(f' row is{row}')
        res = row[0]
        print(res)
    cursor.close()
    return res


def addUser(tg_user_id, first_name, user_name):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("insert into users (tg_id,first_name,user_name) values(?,?,?)",
                   (str(tg_user_id), first_name, user_name,))
    conn.commit()
    cursor.close()
    return getUserId(tg_user_id=tg_user_id)


def addLocation(user_id, longitude, latitude):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("insert into locations (user_id, longitude, latitude)values (?, ?, ? )",
                   (str(user_id), str(longitude), str(latitude),))
    conn.commit()
    cursor.close()

def getLocation(user_id):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("select longitude, latitude from locations where user_id =?",(str(user_id),))
    result= cursor.fetchall()
    return  result
