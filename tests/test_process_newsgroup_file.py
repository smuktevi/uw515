import unittest
import sys
sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')
import newsgroup_analysis as nga

class TestEmailValidity(unittest.TestCase):
    pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailValidity)
_ = unittest.TextTestRunner().run(suite)