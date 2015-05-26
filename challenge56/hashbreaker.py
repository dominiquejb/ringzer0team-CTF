import hashlib
import requests
import re
import binascii
import os

__author__ = 'dBizzle'

s = requests.session()

#url to fetch
baseurl = "http://ringzer0team.com/challenges/56"

#fetch the web page with my PHPSESSID at the time
r = s.post(baseurl, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#find area around the message i need, reduces string size for regex to search in
ibegin = r.content.find("BEGIN HASH -----") + 16 #index+length
iend = r.content.find("----- END HASH") #index
msgsection = r.content[ibegin:iend]

#Extract just the message from the page
msg = re.findall(r"\s+(\w+)<br", msgsection)[0]

#After using online reverse sha1 tools,
# we found that the decrypted hash is an int value with 4 digits (1000-9999)
# let's brute-force it since it's easy to find
for i in xrange(1000,10000):
    if (hashlib.sha1(str(i)).hexdigest() == msg):
        answer = str(i)
        print "answer = " + answer
        break


#fetch the result Web page using the answer in the URL with my PHPSESSID cookie at the time
r = s.post(baseurl + "/{}".format(answer), cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#Extract just the flag from the result webpage
flag = re.findall(r">(FLAG-\w+)<", r.content)
if len(flag)>0:
    print "The flag is : " + flag[0]
else:
    print "No flag found"