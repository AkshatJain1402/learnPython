
#extract valid email addresses
text = "This is an email example: contact@example.com. You can also reach us at support@yourcompany.org. My personal address is not relevant here."

import re
words=[]
s=""
for i in text:
    
    if 64<=ord(i)<90 or 96<ord(i)<122 :
       
        s+=i
        
    else:
        words.append(s)
        s=""
        
for i in words:

    if "@" in i:
        print(i)
    
print(words)

#output ["contact@example.com","support@yourcompany.org"]
#method 2 using built in functions

words=text.split(" ")
for i in words:
    if '@' in i:
        print(i)


#Method 3 using regex


def extract_emails(text):
  """Extracts all valid email addresses from a given text."""
  email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+" 
  emails = re.findall(email_regex, text)
  return emails

text = "This is an email example: contact@example.com. You can also reach us at support@yourcompany.org. My personal address is not relevant here."
emails = extract_emails(text)
print("Extracted email addresses:")
for email in emails:
  print(email)



