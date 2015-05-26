import hashlib
import requests
import re
import binascii

__author__ = 'dBizzle'

s = requests.session()

#url to fetch
baseurl = "http://ringzer0team.com/challenges/14"

#fetch the web page with my PHPSESSID at the time
r = s.post(baseurl, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})

#find area around the message i need, reduces string size for regex to search in
ibegin = r.content.find("BEGIN MESSAGE -----") + 19 #index+length
iend = r.content.find("----- END MESSAGE") #index
mystr = r.content[ibegin:iend]

#Extract just the message from the page
msg1 = re.findall(r"\s+([01]+)<br", mystr)
binaryStr = msg1[0]

#print "test"
msg = ''.join(chr(int(binaryStr[i:i+8],2)) for i in xrange(0, len(binaryStr), 8))

#print "le msg is " + msg

#Hash the message using SHA512
leHash = hashlib.sha512(msg).hexdigest()
#print "le hash is " + leHash

#fetch the result web page with my PHPSESSID at the time
r = s.post(baseurl + "/" + leHash, cookies={'PHPSESSID': 'j3c7p18vekvafqev0cnejq4g53'})
#print r.content
#Extract just the flag from the result webpage
flag = re.findall(r">(FLAG-\w+)<", r.content)

print "The flag is : " + flag[0]