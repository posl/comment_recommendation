def solution(a,b,c,d,e):
    res = 0
    if a%10 > 0:
        res = a + (10 - a%10)
    else:
        res = a
    if b%10 > 0:
        res = min(res, b + (10 - b%10))
    else:
        res = min(res, b)
    if c%10 > 0:
        res = min(res, c + (10 - c%10))
    else:
        res = min(res, c)
    if d%10 > 0:
        res = min(res, d + (10 - d%10))
    else:
        res = min(res, d)
    if e%10 > 0:
        res = min(res, e + (10 - e%10))
    else:
        res = min(res, e)
    return res
