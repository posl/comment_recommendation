def findClosestInt(x, p):
    p.sort()
    if x in p:
        return x
    if len(p) == 0:
        return x
    if x < p[0]:
        return p[0]
    if x > p[-1]:
        return p[-1]
    for i in range(len(p)):
        if x < p[i]:
            if p[i] - x < x - p[i-1]:
                return p[i]
            else:
                return p[i-1]
