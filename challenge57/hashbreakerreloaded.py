import hashlib
import requests
import re

__author__ = 'dBizzle'

s = requests.session()

#url to fetch
baseurl = "http://ringzer0team.com/challenges/57"

#fetch the web page with my PHPSESSID at the time
r = s.post(baseurl, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#find area around the hash, reduces string size for regex to search in
hashbegin = r.content.find("BEGIN HASH -----") + 16 #index+length
hashend = r.content.find("----- END HASH") #index
hashsection = r.content[hashbegin:hashend]

#find area around the salt, reduces string size for regex to search in
saltbegin = r.content.find("BEGIN SALT -----") + 16 #index+length
saltend = r.content.find("----- END SALT") #index
saltsection = r.content[saltbegin:saltend]

#Extract just the hash from the page
theHash = re.findall(r"\s+(\w+)<br", hashsection)[0]
print theHash

#Extract just the salt from the page
salt = re.findall(r"\s+(\w+)<br", saltsection)[0]
print salt

#After using online reverse sha1 tools,
# we found that the decrypted hash is an int value with 4 digits (1000-9999)
# let's brute-force it since it's easy to find
for i in xrange(1000,10000):
    if (hashlib.sha1(str(i)+str(salt)).hexdigest() == theHash):
        answer = str(i)
        print "1answer = " + answer
        break


#fetch the result Web page using the answer in the URL with my PHPSESSID cookie at the time
r = s.post(baseurl + "/{}".format(answer), cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#Extract just the flag from the result webpage
flag = re.findall(r">(FLAG-\w+)<", r.content)
if len(flag)>0:
    print "The flag is : " + flag[0]
else:
    print "No flag found"