#!/usr/bin/env python
# coding: utf-8

# 1. Create a function `check_email_validity` that takes a single argument, a text string, and returns a boolean value. Return true if found to be a valid email, false else.
# 
# [ ] Correct basic logic for email validity using Python string methods and/or lists (regular expressions, e.g. `re`, not allowed for this assignment) [2pts].
# [ ] Correct logic for edge cases and more difficult values [1pt].
# 
# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol. Let's call the first part *personal* and the latter part *domain*, i.e., personal@domain. The length of the personal part may be up to 64 characters long and domain name may be up to 253 characters.
# 
# The personal and domain parts contains the following ASCII characters:
# 
# - Uppercase (`A-Z`) and lowercase (`a-z`) English letters.
# - Digits (`0-9`).
# - Character `-` (dash).
# - Character `.` (period, dot or fullstop) provided that it is not the first or last character and it will not come one after the other.
# 
# Additionally, the personal part can contain:
# 
# - Characters `! # $ % & ' * + / = ? ^ _ { | } ~`
# 
# Example of valid emails:
# 
#     mysite@ourearth.com
#     my.ownsite@ourearth.org
#     mysite@you.me.net
#     mysite123@gmail.b [This is valid, discussion in Canvas]
# 
# Example of invalid emails:
# 
#     mysite.ourearth.com [@ is not present]
#     mysite@.com.my [domain can not start with dot "."]
#     @you.me.net [No character before @]
#     mysite@.org.org [domain can not start with dot "."]
#     .mysite@mysite.org [Personal part can not start with "."]
#     mysite()*@gmail.com [Invalid due to parentheses in personal part, asterisk acceptable]
#     mysite..1234@yahoo.com [double dots are not allowed]

# In[ ]:





# In[12]:


def check_email_validity(email_id) -> bool:
    if not email_id.count("@") == 1:
        return False
    if len(email_id) <=2:         
        return False
    if email_id.find("..") != -1: 
        return False
    personal_n = 64
    domain_n = 253
    personal, domain = email_id.split('@')
    if len(personal) ==0 or len(personal)>personal_n or len(domain)==0 or len(domain)>domain_n:
        return False
    checklist = ".!#$%&\'*+/=?^_{|}~-"
    for k in [personal, domain]:
        if k[-1]=='.' or k[0]=='.':
            return False
        for i in k:
            if k == personal:
                if (i not in checklist) and not i.isalnum():
                        return False
            elif not i.isalnum() and i not in '-.':
                return False
    return True

# print(check_email_validity("wohlmuth@cehpx10"))
# In[13]:
# usn = "s.muktevi2333@aol.com"
# valid = ["mysite@ourearth.com", 
#     "my.ownsite@ourearth.org",
#     "mysite@you.me.net",
#     "mysite123@gmail.b"]
# invalid = [
#      "mysite.ourearth.com",
#     "mysite@.com.my",
#     "@you.me.net" ,
#     ".mysite@mysite.org", 
#     "mysite()*@gmail.com", 
#     "mysite..1234@yahoo.com" 
# ]
# for i in invalid:
#     print(check_email_validity(i))


# Learn how to extract data.
# 

# In[14]:
# import string
# print(string.punctuation)

def process_newsgroup_file(fpath, word_counts):
    # import io
    # import string
    with open(fpath, "r", encoding='windows-1252') as f:
    # with open(fpath, "r+") as f:
        data = f.read()
        data = data.replace('||'," ")
        # data = data.replace(','," ")
        words = data.split()
        valid_email = []
        for i in words:
            if check_email_validity(i):
                if i not in valid_email:
                    # if "<" == i[0] and ">" == i[-1]:
                    #     valid_email.append(i.strip("<>"))
                    # else:
                    valid_email.append(i)
            else:
                for j in i:
                    if not j.isalnum():
                        i = i.replace(j,"")
                # if(i.isalnum()):
                word_counts[i]+=1
    # print(valid_email, word_counts)
    return (valid_email, word_counts)
# In[15]:

# `! # $ % & ' * + / = ? ^ _ { | } ~ . -`
# fpath = "hw2.txt"
# word_counts = defaultdict(int)
# final = process_newsgroup_file(fpath, word_counts)

# In[34]:


def process_newsgroup_topic(dir_path):
    from collections import defaultdict
    import glob
    import pickle
    word_list=defaultdict(int)
    valids = []
    files = glob.glob(dir_path)
    for i in files:
        emails, word_list = process_newsgroup_file(i, word_list)
        valids.extend(emails)
    with open("sci.crypt.emails.txt", "w+") as f:
        f.write('\n'.join(valids))
    with open("sci.crypt.wordcounts.pkl",'wb') as f1:
        pickle.dump(word_list, f1)


# In[35]:


# process_newsgroup_topic("20_newsgroups/sci.crypt/*")
# print("<SLKDFNHLS>".strip("<>"))
