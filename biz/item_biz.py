#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # NOQA: E402
sys.path.append('.')  # NOQA: E402

from db import role_item_data
from db import item_cast_data
from db import player_item_data
from db import item_data


class ItemQuantity:
    def __init__(self, item_code, quantity):
        self.item_code = item_code
        self.quantity = quantity

    def __repr__(self):
        return f"ItemQuantity(item_code={self.item_code}, quantity={self.quantity})"


def contrast_item_by_role(role_code):
    # 查询item转换关系
    item_casts = item_cast_data.query_all()
    # 以from为key的map
    item_cast_map = {}
    for ic in item_casts:
        item_cast_map[ic.from_code] = ic
    # 转换
    (item_quantitys, item_quantity_map) = _convert_role_item(item_cast_map, role_code)
    # 查询已有item
    (exist_item_quantitys, exist_item_quantity_map) = _convert_play_item(item_cast_map, role_code)
    item_map = item_data.get_items_by_codes(item_quantity_map.keys())
    for iq in item_quantitys:
        exist_iq = exist_item_quantity_map.get(iq.item_code, ItemQuantity(iq.item_code, 0))
        print(f'{item_map.get(iq.item_code).name}\t需求:{iq.quantity}\t已有:{exist_iq.quantity}')


def _convert_role_item(item_cast_map, role_code):
    role_items = role_item_data.get_by_role_code(role_code)
    item_quantitys = []
    item_quantity_map = {}
    for ri in role_items:
        # 判断是否可转换
        iq = _cast_item(item_cast_map, ItemQuantity(ri.item_code, ri.quantity))
        if iq.item_code in item_quantity_map:
            old = item_quantity_map.get(iq.item_code)
            old.quantity += iq.quantity
        else:
            item_quantitys.append(iq)
            item_quantity_map[iq.item_code] = iq
    return (item_quantitys, item_quantity_map)


def _convert_play_item(item_cast_map, role_code):
    player_items = player_item_data.get_by_role_code(role_code)
    item_quantitys = []
    item_quantity_map = {}
    for pi in player_items:
        # 判断是否可转换
        iq = _cast_item(item_cast_map, ItemQuantity(pi.item_code, pi.quantity))
        if iq.item_code in item_quantity_map:
            old = item_quantity_map.get(iq.item_code)
            old.quantity += iq.quantity
        else:
            item_quantitys.append(iq)
            item_quantity_map[iq.item_code] = iq
    return (item_quantitys, item_quantity_map)


def _cast_item(item_cast_map, iq):
    item_cast = item_cast_map.get(iq.item_code)
    if item_cast == None:
        return iq
    return _cast_item(item_cast_map, ItemQuantity(item_cast.to_code, iq.quantity * item_cast.rate))
