def solve(n, m, a):
    m = sorted(a)
    m.reverse()
    ans = ""
    while n > 0:
        for i in range(len(m)):
            if n >= m[i]:
                ans += str(m[i])
                n -= m[i]
                break
    return ans
