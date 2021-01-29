import unittest
import sys
# sys.path.insert(1, 'E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/')
import newsgroup_analysis as nga

class TestNewsGroupAnalysis(unittest.TestCase):
    def check_file_format(self, file_data):
            valid_email_format = {"From:":0, "Date:":0, "Subject:":0}
            for line in file_data:
                words = line.split()
                if len(words)>0:
                    if words[0] in valid_email_format:
                        valid_email_format[words[0]] = 1
                    if len(words) == 1 and words[0] == '\n':
                        break
                if sum(valid_email_format.values())==3:
                    return True
            return False

    def test_checkemail_at(self):
        """confirm that check_email_validity() checks for @ sign"""
        self.assertFalse(nga.check_email_validity("emailnoat.com"))
        self.assertFalse(nga.check_email_validity("email@noat.c@om"))
    
    def test_emailformaterror(self):
        """confirm that a non-email format raises EmailFormatError"""
        with self.assertRaises(nga.EmailFormatError):
            nga.process_newsgroup_file("Homework/uw515/tests/for_tests/not_email.txt", {})

        #valid case
        # with open("Homework/uw515/tests/for_tests/email.txt", encoding="windows-1252") as f:
        #     try:
        #         data = f.readlines()
        #         self.assertTrue(check_file_format(data))
        #     except:
        #         raise EmailFormatError("Wrong file format sent! File must be in Email format.")

        # #invalid case
        # with open("Homework/uw515/tests/for_tests/not_email.txt", encoding="windows-1252") as f:
        #     try:
        #         data = f.readlines()
        #         self.assertFalse(check_file_format(data))
        #     except:
        #         raise EmailFormatError("Wrong file format sent! File must be in Email format.")


         # try:
    #     if not check_file_format(data):
    #         raise EmailFormatError("Wrong file format sent! File must be in Email format.")
    # except EmailFormatError as e:
    #     print(e.message)
    #     return (valid_emails, None)
    # except:
    #     print("Another Issue Raised!")
    #     return (valid_emails, None)
    # def test_email_validity(self):
    #     """
    #     Invokes check_email_validity funciton with different test cases
    #     """
    #     def one_shot_test(valid_email, message=""):
    #         """
    #         Checks email validity function for valid email test cases.
    #         """
    #         try:
    #             self.assertTrue(nga.check_email_validity(valid_email))
    #         except:
    #             raise RuntimeError("The check_email_validity() did not pass for valid test case: ",valid_email, message)

    #     def edge_test(invalid_email, message=""):
    #         """
    #         Checks email validity function for invalid email "edge" cases.
    #         """
    #         try:
    #             self.assertFalse(nga.check_email_validity(invalid_email))
    #         except:
    #             raise RuntimeError("The check_email_validity() passed for an invalid test case: ", invalid_email, message)

    #     one_shot_test("abc!!!#@aol.com")
    #     one_shot_test("abc12reg34##!*&@gmail.com")    
    #     one_shot_test("abcdef12345@gmail.com")    
    #     one_shot_test("abc-asd.asd@asd.com")
    #     edge_test("121212121@")
    #     edge_test("1^%$!@*^$#@^#$@!&^#@*%#!%$#*&^%")
    #     edge_test("abcdef", "Does not check for @ sign")
    #     edge_test("kfsjn12408172u98-29524-5u82039u09023509")
    #     print("Email Address Validity Test: PASSED")
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestNewsGroupAnalysis)
_ = unittest.TextTestRunner().run(suite)

