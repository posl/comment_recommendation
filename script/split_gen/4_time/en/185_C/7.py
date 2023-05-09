def cut(l):
    if l == 0:
        return 1
    if l <= 11:
        return 0
    return sum([cut(l-i) for i in range(1, 12)])
