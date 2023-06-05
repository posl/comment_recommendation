def get_x(n, x, p):
    if n == 0:
        return x
    else:
        p.sort()
        if x in p:
            return get_x(n, x-1, p)
        else:
            for i in range(1, x):
                if x - i in p:
                    return x - i
                elif x + i in p:
                    return x + i
