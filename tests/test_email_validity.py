import unittest
import sys
# sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')

import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import newsgroup_analysis as nga
class TestNewsGroupAnalysis(unittest.TestCase):

    def test_checkemail_at(self):
        """confirm that check_email_validity() checks for @ sign"""
        self.assertFalse(nga.check_email_validity("emailnoat.com"),"missing the @ symbol")
        self.assertFalse(nga.check_email_validity("email@noat.c@om"), "2 @ symbols")
    
    def test_emailformaterror(self):
        """confirm that a non-email format raises EmailFormatError"""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with self.assertRaises(nga.EmailFormatError):
            nga.process_newsgroup_file(os.path.join(__location__, 'not_email.txt'), {})


suite = unittest.TestLoader().loadTestsFromTestCase(TestNewsGroupAnalysis)
_ = unittest.TextTestRunner().run(suite)

