import hashlib
import requests
import re
import binascii

__author__ = 'dBizzle'

s = requests.session()

#url to fetch
baseurl = "http://ringzer0team.com/challenges/32"

#fetch the web page with my PHPSESSID at the time
r = s.post(baseurl, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#find area around the message i need, reduces string size for regex to search in
ibegin = r.content.find("BEGIN MESSAGE -----") + 19 #index+length
iend = r.content.find("----- END MESSAGE") #index
msgsection = r.content[ibegin:iend]
print msgsection

#Extract just the message from the page
msg = re.findall(r"\s+((\d+)\s\+\s(\w+)\s\-\s(\d+))\s=\s\?<br", msgsection)[0]

#compute the mathematical equation
#val  = decimal     + hex           - binary
value = int(msg[1]) + int(msg[2],0) - int(msg[3],2)

#fetch the result web page with my PHPSESSID at the time
r = s.post(baseurl + "/{}".format(value), cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})
print r.content
#Extract just the flag from the result webpage
flag = re.findall(r">(FLAG-\w+)<", r.content)

print "The flag is : " + flag[0]