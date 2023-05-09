def get_permutation(n, r):
    if n < r:
        return []
    elif r == 0:
        return [[]]
    else:
        ret = []
        for i in range(n):
            s = get_permutation(n - 1, r - 1)
            for x in s:
                ret.append(x[:i] + [n - 1] + x[i:])
        return ret
