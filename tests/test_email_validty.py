import unittest
import sys
sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')
import newsgroup_analysis as nga

class TestEmailValidity(unittest.TestCase):

    def test_email_validity(self):
        """
        Invokes check_email_validity funciton with different test cases
        """
        def one_shot_test(valid_email, message=""):
            """
            Checks email validity function for valid email test cases.
            """
            try:
                self.assertTrue(nga.check_email_validity(valid_email))
            except:
                raise RuntimeError("The check_email_validity() did not pass for valid test case: ",valid_email, message)

        def edge_test(invalid_email, message=""):
            """
            Checks email validity function for invalid email "edge" cases.
            """
            try:
                self.assertFalse(nga.check_email_validity(invalid_email))
            except:
                raise RuntimeError("The check_email_validity() passed for an invalid test case: ", invalid_email, message)

        one_shot_test("abc!!!#@aol.com")
        one_shot_test("abc12reg34##!*&@gmail.com")    
        one_shot_test("abcdef12345@gmail.com")    
        one_shot_test("abc-asd.asd@asd.com")
        edge_test("121212121@")
        edge_test("1^%$!@*^$#@^#$@!&^#@*%#!%$#*&^%")
        edge_test("abcdef", "Does not check for @ sign")
        edge_test("kfsjn12408172u98-29524-5u82039u09023509")
        print("Email Address Validity Test: PASSED")
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailValidity)
_ = unittest.TextTestRunner().run(suite)

