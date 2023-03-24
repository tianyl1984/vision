#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # NOQA: E402
sys.path.append('.')  # NOQA: E402

import unittest
from db import item_data

class ItemDataTest(unittest.TestCase):

    def test_get_items_by_type(self):
        items = item_data.get_items_by_type(1)
        print(items)
        self.assertTrue(len(items) > 0)

if __name__ == '__main__':
    unittest.main()