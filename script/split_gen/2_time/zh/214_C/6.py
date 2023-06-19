def solve(n, s, t):
    #print(n, s, t)
    for i in range(n):
        if s[i] < t[i]:
            s[i] += 10**9
    #print(s)
    for i in range(1, n):
        s[i] = min(s[i], s[i-1]+t[i-1])
    #print(s)
    return s
