def is_polygon(n, l):
    sum = 0
    max = 0
    for i in range(n):
        sum += l[i]
        if l[i] > max:
            max = l[i]
    if max < sum - max:
        return "是"
    else:
        return "否"
