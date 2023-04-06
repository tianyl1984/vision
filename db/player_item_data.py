from db import db_util
import time

class PlayerItem:
    def __init__(self, id, item_code, quantity, update_time):
        self.id = id
        self.item_code = item_code
        self.quantity = quantity
        self.update_time = update_time

    def __repr__(self):
        return f"PlayerItem(id={self.id}, item_code={self.item_code}, quantity={self.quantity}, update_time={self.update_time})"


def convert(row):
    return PlayerItem(row[0], row[1], row[2], row[3])


def update_quantity(item_code, quantity):
    update_time = int(time.time())
    # 查询是否存在
    sql = "SELECT * FROM player_item WHERE item_code=?"
    exist = db_util.query_one(convert, sql, item_code)
    if exist == None:
        # 保存
        sql = "INSERT INTO player_item (item_code, quantity, update_time) VALUES (?, ?, ?)"
        db_util.execute(sql, item_code, quantity, update_time)
    else:
        sql = "UPDATE player_item SET quantity=?,update_time=? WHERE item_code=?"
        db_util.execute(sql, quantity, update_time, item_code)

def get_by_role_code(role_code):
    sql = "SELECT * FROM player_item WHERE item_code in (SELECT item_code FROM role_item WHERE role_code = ?)"
    return db_util.query_list(convert, sql, role_code)
