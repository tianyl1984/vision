#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # NOQA: E402
sys.path.append('.')  # NOQA: E402

import unittest
from db import player_item_data


class PlayerItemDataTest(unittest.TestCase):

    def test_update_quantity(self):
        ret = player_item_data.update_quantity(1, 15)
        self.assertIsNone(ret)


if __name__ == '__main__':
    unittest.main()
