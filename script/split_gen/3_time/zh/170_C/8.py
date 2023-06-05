def find_nearest(x, p):
    if len(p) == 0:
        return x
    else:
        p.append(x)
        p.sort()
        i = p.index(x)
        if i == 0:
            return p[1]
        elif i == len(p) - 1:
            return p[len(p) - 2]
        else:
            return p[i + 1] if x - p[i - 1] > p[i + 1] - x else p[i - 1]
