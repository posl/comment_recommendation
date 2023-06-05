def rotate90(S):
    return list(map(list,zip(*S[::-1])))
