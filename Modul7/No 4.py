# No 4
import re

wikipedia = open('KEI.html', 'r', encoding='latin1')

text = wikipedia.read()
wikipedia.close()

search = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', text)

list = []
for i in search:
    b = (i[0],float(i[4]))
    list.append(b)
    
print(list)

