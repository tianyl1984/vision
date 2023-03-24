from db import db_util


class Item:
    def __init__(self, id, code, name, type):
        self.id = id
        self.code = code
        self.name = name
        self.type = type
    def __str__(self):
        return f"Item(id={self.id}, code={self.code}, name={self.name}, type={self.type})"

def convert(row):
    return Item(row[0], row[1], row[2], row[3])

def get_items_by_type(item_type):
    sql = "SELECT * FROM item WHERE type=?"
    return db_util.query_list(convert, sql, item_type)
