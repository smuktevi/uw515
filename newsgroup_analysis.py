def check_email_validity(email_id):
    if '@' not in  email_id or ".." in email_id or len(email_id)<=2:
        return False
    if email_id.count("@")>1:
        return False
    personal, domain = email_id.split("@")
    if len(personal)>64 or len(domain)>253 or len(personal)==0 or len(domain)==0:
        return False
    checklist = ".!#$%&\'*+/=?^_{|}~-"
    for part in [personal, domain]:
        if part[0]=='.' or part[-1]=='.':
            return False
    for ch in personal:
        if ch not in checklist and not ch.isalnum():
            return False
    for ch in domain:
        if not ch.isalnum() and ch not in "-.":
            return False 
    return True

def process_newsgroup_file(path, word_counts):
    valid_emails=[]
    with open(path, encoding="windows-1252") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if check_email_validity(word):
                    if word not in valid_emails:
                        valid_emails.append(word)
                else:
                    word = word.strip()
                    for ch in word:
                        if not ch.isalnum():
                            word = word.replace(ch,"")
                    if word in word_counts:
                        word_counts[word]+=1
                    else:
                        word_counts[word]=1
    return (valid_emails,word_counts)


def process_newsgroup_topic(dpath):
    import glob
    import pickle
    word_counts={}
    valid_emails=[]
    files = glob.glob(dpath)
    for file in files:
        emails, word_counts = process_newsgroup_file(file, word_counts)
        valid_emails.extend(emails)
    with open("sci.crypt.emails.txt", "w+") as f:
        f.write('\n'.join(valid_emails))
    with open("sci.crypt.wordcounts.pkl",'wb') as f1:
        pickle.dump(word_counts, f1)

# process_newsgroup_file("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/for_tests/not_email.txt", {})
# process_newsgroup_file("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/for_tests/emails/16351", {})

# process_newsgroup_topic("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/for_tests/emails")
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