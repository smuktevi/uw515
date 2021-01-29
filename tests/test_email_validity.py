import unittest
import sys
# sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')
import newsgroup_analysis as nga

class EmailFormatError(Exception):
    """Raised when a file passed to the function is not in an Email format"""
    def __init__(self, message):
        self.message = message

class TestNewsGroupAnalysis(unittest.TestCase):

    def test_checkemail_at(self):
        """confirm that check_email_validity() checks for @ sign"""
        self.assertFalse(nga.check_email_validity("emailnoat.com"))
        self.assertFalse(nga.check_email_validity("email@noat.c@om"))
    
    def test_emailformaterror(self):
        """confirm that a non-email format raises EmailFormatError"""
        with self.assertRaises(EmailFormatError):
            if not nga.process_newsgroup_file("Homework/uw515/tests/not_email.txt", {}):
                raise EmailFormatError("Wrong file format sent! File must be in Email format.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestNewsGroupAnalysis)
_ = unittest.TextTestRunner().run(suite)

