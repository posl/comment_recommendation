def judgePolygon(L):
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        return "是"
    else:
        return "否"
