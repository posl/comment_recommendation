def diff(s, t):
    n = len(s)
    m = len(t)
    ans = n
    for i in range(n-m+1):
        tmp = 0
        for j in range(m):
            if s[i+j] != t[j]:
                tmp += 1
        ans = min(ans, tmp)
    return ans
