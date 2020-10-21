import os
import re
from urllib.parse import urlparse
 
array = []

register_file = open('register.txt')
lines = register_file.readlines()

for i in range(1, len(lines)):#1
    b = lines[i].strip().split(';')
    array.extend(b)
 
url = input("Enter URL: ")
if url in array:
    print("URL is blocked")
else:
    print("URL insn't bloked")
 
parse = urlparse(url)#2
domain = parse.netloc.split(".")[1:]
server = ".".join(domain)
print("DOMAIN:",server)
 
if server in array:
    print("In the list")
else:
    print("Isn't in the list")
