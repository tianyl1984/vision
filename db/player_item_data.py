from db import db_util
import time

class PlayerItem:
    def __init__(self, id, item_id, quantity, update_time):
        self.id = id
        self.item_id = item_id
        self.quantity = quantity
        self.update_time = update_time

    def __str__(self):
        return f"PlayerItem(id={self.id}, item_id={self.item_id}, quantity={self.quantity}, update_time={self.update_time})"


def convert(row):
    return PlayerItem(row[0], row[1], row[2], row[3])


def update_quantity(item_id, quantity):
    update_time = int(time.time())
    # 查询是否存在
    sql = "SELECT * FROM player_item WHERE item_id=?"
    exist = db_util.query_one(convert, sql, item_id)
    if exist == None:
        # 保存
        sql = "INSERT INTO player_item (item_id, quantity, update_time) VALUES (?, ?, ?)"
        db_util.execute(sql, item_id, quantity, update_time)
    else:
        sql = "UPDATE player_item SET quantity=?,update_time=? WHERE item_id=?"
        db_util.execute(sql, quantity, update_time, item_id)

