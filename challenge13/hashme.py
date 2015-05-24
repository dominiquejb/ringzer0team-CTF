import hashlib
import requests
import re

__author__ = 'dBizzle'

s = requests.session()

#url to fetch
baseurl = "http://ringzer0team.com/challenges/13"

#fetch the web page with my PHPSESSID at the time
r = s.post(baseurl, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#find area around the message i need, reduces string size for regex to search in
ibegin = r.content.find("BEGIN MESSAGE -----") + 19 #index+length
iend = r.content.find("----- END MESSAGE") #index
mystr = r.content[ibegin:iend]

#Extract just the message from the page
msg1 = re.findall(r"\s+(\w+)<br", mystr)

#Hash the message using SHA512
leHash = hashlib.sha512(msg1[0]).hexdigest()

#fetch the result web page with my PHPSESSID at the time
r = s.post(baseurl + "/" + leHash, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})
#Extract just the flag from the result webpage
flag = re.findall(r">(FLAG-\w+)<", r.content)

print "The flag is : " + flag[0]