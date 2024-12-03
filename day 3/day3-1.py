import re

with open('day 3/day3.txt', 'r') as f:
    content = f.read()

pattern = r'mul\(([0-9]+),([0-9]+)\)'
mults = re.findall(pattern, content)

out = 0

for mult in mults:
    lnum, rnum = mult
    out += int(lnum) * int(rnum)

print(out)