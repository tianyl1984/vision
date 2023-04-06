from db import db_util

class RoleItem:
    def __init__(self, id, role_code, item_code, quantity):
        self.id = id
        self.role_code = role_code
        self.item_code = item_code
        self.quantity = quantity

    def __repr__(self):
        return f"RoleItem(id={self.id}, role_code='{self.role_code}', item_code={self.item_code}, quantity={self.quantity})"

def convert(row):
    return RoleItem(row[0], row[1], row[2], row[3])

def get_by_role_code(role_code):
    sql = "SELECT * FROM role_item WHERE role_code=?"
    return db_util.query_list(convert, sql, role_code)