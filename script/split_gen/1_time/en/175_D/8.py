def solve(n, k, p, c):
    ans = -10**18
    for i in range(n):
        #print("i:", i)
        j = i
        s = 0
        m = 0
        while True:
            #print("j:", j)
            j = p[j] - 1
            s += c[j]
            m += 1
            if j == i:
                break
        if s > 0:
            #print("s:", s)
            #print("m:", m)
            t = (k - m) // m
            #print("t:", t)
            ans = max(ans, s * t + max(0, max(c[:j+1]) * (k - m - t * m)))
        else:
            ans = max(ans, max(c[:j+1]) * k)
    return ans
