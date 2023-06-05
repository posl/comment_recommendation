def f(n,m,as_):
    if m == 0:
        return 1
    as_.sort()
    if as_[0] != 1:
        as_.insert(0,0)
    if as_[-1] != n:
        as_.append(n+1)
    w = []
    for i in range(1,len(as_)):
        w.append(as_[i] - as_[i-1] - 1)
    k = min(w)
    if k == 0:
        return 0
    ans = 0
    for i in w:
        ans += (i + k - 1) // k
    return ans
