#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # NOQA: E402
sys.path.append('.')  # NOQA: E402

import unittest
from biz import item_biz

class Item_Biz_Test(unittest.TestCase):

    def test_contrast_item_by_role(self):
        item_biz.contrast_item_by_role('C001')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
