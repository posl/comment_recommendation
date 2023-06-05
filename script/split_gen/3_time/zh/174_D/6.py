def min_op(s):
    l = len(s)
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        return 0
    if r == w:
        return 2
    if r > w:
        return w
    if w > r:
        return r
