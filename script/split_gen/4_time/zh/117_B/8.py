def check_polygon(n, l):
    sum = 0
    max = 0
    for i in range(n):
        if l[i] > max:
            max = l[i]
        sum += l[i]
    if max < sum - max:
        print("是")
    else:
        print("否")
