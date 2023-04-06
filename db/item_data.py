from db import db_util


class Item:
    def __init__(self, id, code, name, type):
        self.id = id
        self.code = code
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Item(id={self.id}, code={self.code}, name={self.name}, type={self.type})"


def convert(row):
    return Item(row[0], row[1], row[2], row[3])


def get_items_by_type(item_type):
    sql = "SELECT * FROM item WHERE type=?"
    return db_util.query_list(convert, sql, item_type)


def get_items_by_codes(codes):
    if len(codes) == 0:
        return {}
    sql = "SELECT * FROM item WHERE code in " + db_util.in_query(codes)
    items = db_util.query_list(convert, sql, *codes)
    item_map = {}
    for it in items:
        item_map[it.code] = it
    return item_map
