import sqlite3

conn = sqlite3.connect('vision.db')
cursor = conn.cursor()


def _with_conn(cb, *args):
    conn = sqlite3.connect('vision.db')
    cur = conn.cursor()
    try:
        return cb(conn, cur, *args)
    finally:
        conn.close()


def _fetchall(conn, cur, *args):
    sql = args[0]
    # print(sql, (args[1]))
    cur.execute(sql, (args[1]))
    return cur.fetchall()


def query_list(cb, sql, *args):
    rows = _with_conn(_fetchall, sql, args)
    result = []
    for row in rows:
        result.append(cb(row))
    return result


def query_one(cb, sql, *args):
    items = query_list(cb, sql, *args)
    if len(items) == 0:
        return None
    return items[0]

def _execute(conn, cur, *args):
    sql = args[0]
    cur.execute(sql, (args[1]))
    conn.commit()
    

def execute(sql, *args):
    _with_conn(_execute, sql, args)

def in_query(params):
    return "(" + ",".join(["?" for i in range(len(params))]) + ")"
