#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        #有効な場合
        def test_valid_case1(self):
                self.assertEqual(1, calc(1, 1))
        def test_valid_case2(self):
                self.assertEqual(998001, calc(999, 999))
        def test_valid_case3(self):
                self.assertEqual(56088, calc(123, 456))
        #範囲外
        def test_out_of_range1(self):
                self.assertEqual(-1, calc(0, 500))
        def test_out_of_range2(self):
                self.assertEqual(-1, calc(1000, 500))
        def test_out_of_range3(self):
                self.assertEqual(-1, calc(999.4, 500))
        #文字列
        def test_string_input1(self):
                self.assertEqual(-1, calc('a', 999))
        def test_string_input2(self):
                self.assertEqual(-1, calc('1a', 2))
        #全角数字
        def test_special_char_input(self):
                self.assertEqual(-1, calc('１０', 5))
        #空白
        def test_empty_input(self):
                self.assertEqual(-1, calc('', 100))
        def aaa2(self):
                self.assertEqual(-1, calc(1002, 500))

