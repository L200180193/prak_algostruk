# No 1
import re

a = open("Indonesia.txt", 'r', encoding='latin1')

text = a.read()
a.close()
x = r'me\w+'
tampilkan = re.findall(x,text)

print(tampilkan)
