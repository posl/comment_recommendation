def get_min_mp(n, a, b, c, l):
    if n == 0:
        return 0 if a == b == c == 0 else float('inf')
    ret = float('inf')
    ret = min(ret, get_min_mp(n-1, a, b, c, l) + 10)
    if a > 0:
        ret = min(ret, get_min_mp(n-1, a-l[n-1], b, c, l) + 10)
    if b > 0:
        ret = min(ret, get_min_mp(n-1, a, b-l[n-1], c, l) + 10)
    if c > 0:
        ret = min(ret, get_min_mp(n-1, a, b, c-l[n-1], l) + 10)
    ret = min(ret, get_min_mp(n-1, a, b, c, l) + 1)
    if a > 0:
        ret = min(ret, get_min_mp(n-1, a-min(l[n-1], a), b, c, l) + 1)
    if b > 0:
        ret = min(ret, get_min_mp(n-1, a, b-min(l[n-1], b), c, l) + 1)
    if c > 0:
        ret = min(ret, get_min_mp(n-1, a, b, c-min(l[n-1], c), l) + 1)
    return ret
