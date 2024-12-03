with open("./day1.txt", 'r') as f:
    left = {}
    right = {}
    for line in f:
        numbers = line.split("   ")
        if int(numbers[0]) in left.keys():
            left[int(numbers[0])] += 1
        else:
            left[int(numbers[0])] = 1

        if int(numbers[1]) in right.keys():
            right[int(numbers[1])] += 1
        else:
            right[int(numbers[1])] = 1

    output = 0

    for num in left.keys():
        if num in right.keys():
            output += left[num] * right[num] * num
    
    print(output)



