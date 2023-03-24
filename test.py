from db import db_util
from db import item_data
from db import player_item_data

# items = item_data.get_items_by_type(1)
# for temp in items:
#     print(temp)

# print(items[0].name)

player_item_data.update_quantity(1, 10)
