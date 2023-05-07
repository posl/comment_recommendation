def solve(N, K, P, C):
    res = -float("inf")
    for i in range(N):
        s = 0
        t = 0
        j = i
        while True:
            s += C[P[j]-1]
            t += 1
            j = P[j]-1
            if j == i:
                break
        if s > 0:
            if K >= t:
                res = max(res, s*((K-t)//t)+max(0, s))
            else:
                res = max(res, max(C[:t]))
        else:
            res = max(res, max(C[:t]))
    return res
