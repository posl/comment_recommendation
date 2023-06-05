def split(n):
    if n < 10:
        return [[n]]
    else:
        ret = []
        for i in range(1, len(str(n))):
            a = int(str(n)[:i])
            b = int(str(n)[i:])
            if a > 0 and b > 0:
                ret.append([a, b])
        return ret
