import unittest
import sys
# sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')

import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import newsgroup_analysis as nga
class TestNewsGroupAnalysis(unittest.TestCase):

    # def test_checkemail_at(self):
    #     """confirm that check_email_validity() checks for @ sign"""
    #     self.assertFalse(nga.check_email_validity("emailnoat.com"),"missing the @ symbol")
    #     self.assertFalse(nga.check_email_validity("email@noat.c@om"), "2 @ symbols")
    
    def test_emailformaterror(self):
        """confirm that a non-email format raises EmailFormatError"""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, 'not_email.txt')
        with self.assertRaises(nga.EmailFormatError):
            nga.process_newsgroup_file(path, {})

    def test_emailformaterror_not_raised(self):
        """confirm that another issue raises another RunTimeError but not EmailFormatError"""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, 'bad.txt')
        with self.assertRaises(FileNotFoundError):
            nga.process_newsgroup_file(path, {})
    
    def test_nonempty_wordcount(self):
        """confirm that process_newsgroup_file() fails to increment non-zero word count."""
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, 'check_wc.txt')
        old_word_counts = {"three": 1, "one":1}
        temp = old_word_counts.copy()
        _, new_word_counts = nga.process_newsgroup_file(path, old_word_counts)
        self.assertTrue(temp["three"]<new_word_counts["three"])



suite = unittest.TestLoader().loadTestsFromTestCase(TestNewsGroupAnalysis)
_ = unittest.TextTestRunner().run(suite)