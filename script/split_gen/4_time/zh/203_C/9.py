def solve(n, k, ab):
    ab.sort(key=lambda x: x[0])
    for a, b in ab:
        if k < a:
            break
        else:
            k += b
    return k
