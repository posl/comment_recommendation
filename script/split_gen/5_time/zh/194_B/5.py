def min_time(works):
    works.sort(key=lambda x: x[0] + x[1])
    return works[-1][0] + works[-2][1]
