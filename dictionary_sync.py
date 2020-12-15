import re

with open('dictionary_ED.txt', 'r') as f:
    txt = f.readlines()
dc = {}

rem = re.compile('- (.*?) = (.*)')
for i in txt:
    m = re.match(rem, i)
    if m:
        m = m.groups()
        dc[m[0]] = m[1]

print(dc)

with open('dictionary_DE.txt', 'w') as f:
    for i in sorted(dc.keys()):
        f.write(f'{i} = {dc[i]}\n')
