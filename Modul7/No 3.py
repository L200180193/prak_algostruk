# No 3
import re

a = open("Indonesia.txt", 'r', encoding='latin1')

text = a.read()
a.close()
x = r'di \w+'
tampilkan = re.findall(x,text)

print(tampilkan)
