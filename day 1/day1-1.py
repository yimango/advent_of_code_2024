with open("./day1.txt", 'r') as f:
    left = []
    right = []
    for line in f:
        numbers = line.split("   ")
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

left = sorted(left)
right = sorted(right)
out = 0
for x, y in zip(left, right):
    out += abs(x - y)
print(out)
