def solve(n):
    ret = []
    for i in range(1, 2**15):
        if n & i == i:
            ret.append(i)
    return ret
