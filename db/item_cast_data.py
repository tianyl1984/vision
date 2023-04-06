from db import db_util

class ItemCast:
    def __init__(self, id, from_code, to_code, rate):
        self.id = id
        self.from_code = from_code
        self.to_code = to_code
        self.rate = rate

    def __repr__(self):
        return f"ItemCast(id={self.id}, from_code='{self.from_code}', to_code='{self.to_code}', rate={self.rate})"

def convert(row):
    return ItemCast(row[0], row[1], row[2], row[3])

def query_by_from(froms):
    if (len(froms) == 0):
        return []
    sql = "SELECT * FROM item_cast WHERE from_code in " + db_util.in_query(froms)
    return db_util.query_list(convert, sql, froms)

def query_all():
    sql = "SELECT * FROM item_cast"
    return db_util.query_list(convert, sql)