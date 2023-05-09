def rotate(figure):
    return list(map(list,zip(*figure[::-1])))
