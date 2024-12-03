def isvalid(report):
    if 3 >= int(report[0]) - int(report[1]) > 0:
        for i in range(len(report) - 1):
            if not (3 >= int(report[i]) - int(report[i+1]) > 0):
                return False
    elif -3 <= int(report[0]) - int(report[1]) < 0:
        for i in range(len(report) - 1):
            if not (-3 <= int(report[i]) - int(report[i+1]) < 0):
                return False
    else:
        return False
    return True


with open('./day2.txt', 'r') as f:
    reports = [line.strip().split(' ') for line in f]

out = 0

for report in reports:
    inc_vio = set()
    dec_vio = set()

    for i in range(len(report) - 1):
        if not (3 >= int(report[i]) - int(report[i+1]) > 0):
            inc_vio.update({i, i+1})

        if not (-3 <= int(report[i]) - int(report[i+1]) < 0):
            dec_vio.update({i, i+1})

    if not inc_vio or not dec_vio:
        out += 1
    else:
        total_vios = inc_vio | dec_vio
        for i in total_vios:
            if isvalid(report[:i] + report[i+1:]):
                out += 1
                break

print(out)
