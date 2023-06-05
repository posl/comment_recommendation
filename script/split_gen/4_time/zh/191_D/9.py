def get_point_num(x, y, r):
    # print(x, y, r)
    if r.is_integer():
        r = int(r)
    else:
        r = int(r) + 1
    x = int(x * 10000)
    y = int(y * 10000)
    # print(x, y, r)
    # print(r ** 2)
    # print((x - r) ** 2)
    # print((x + r) ** 2)
    # print((y - r) ** 2)
    # print((y + r) ** 2)
    num = 0
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                num += 1
    return num
