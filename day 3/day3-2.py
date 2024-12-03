import re

with open('day 3/day3.txt', 'r') as f:
    content = f.read()

pattern = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'
commands = re.findall(pattern, content)

out = 0
counts = True

for command in commands:
    if command == "do()":
        counts = True
    elif command == "don't()":
        counts = False
    else:
        if counts:
            nums = re.findall(r'[0-9]+', command)
            out += int(nums[0]) * int(nums[1])

print(out)