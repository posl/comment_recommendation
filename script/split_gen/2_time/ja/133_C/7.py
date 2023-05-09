def mod2019(l, r):
    if r - l >= 2019:
        return 0
    else:
        min = 2019
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                if min > (i * j) % 2019:
                    min = (i * j) % 2019
        return min
