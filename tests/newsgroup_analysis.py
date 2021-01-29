
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

def check_file_format(file_data):
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

def process_newsgroup_file(path, word_counts):
    valid_emails=[]
    with open(path, encoding="windows-1252") as f:
        data = f.readlines()
        if not check_file_format(data):
            return False
        # except EmailFormatError as e:
        #     print(e)
        #     return (valid_emails, None)
        # except:
        #     print("Another Issue Raised!")
        #     return (valid_emails, None)
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

process_newsgroup_file("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/not_email.txt", {})
# process_newsgroup_file("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/for_tests/emails/16351", {})

# process_newsgroup_topic("E:/UW/UW_WINTER_Materials_2020/Data 557/Week 2/Homework/uw515/tests/for_tests/emails")