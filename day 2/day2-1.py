with open('./day2.txt', 'r') as f:
    reports = []
    for line in f:
        reports.append(line.split(' '))

out = 0

for report in reports:
    if 3 >= int(report[0]) - int(report[1]) > 0:
        for i in range(len(report) - 1):
            if not (3 >= int(report[i]) - int(report[i+1]) > 0):
                out -= 1
                break
        out +=1
    elif -3 <= int(report[0]) - int(report[1]) < 0:
        for i in range(len(report) - 1):
            if not (-3 <= int(report[i]) - int(report[i+1]) < 0):
                out -= 1
                break
        out +=1
print(out)