def f(n, k, a):
    a.sort()
    a = [x for x in a if x < 0]
    b = [x for x in a if x >= 0]
    a.reverse()
    if k <= len(a) * len(b):
        return 0
    else:
        k -= len(a) * len(b)
    while len(a) > 0 and len(b) > 0:
        if k == 1:
            return a[0] * b[0]
        elif k == 2:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1], b[0] * b[1])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
        elif k == 3:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1] * a[2], b[0] * b[1] * b[2])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
        else:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1], b[0] * b[1])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
    return 0
