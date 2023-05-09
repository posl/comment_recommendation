def solve(s,t):
    n = len(s)
    m = len(t)
    res = m
    for i in range(n-m+1):
        cur = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cur += 1
        res = min(res,cur)
    return res
s = input()
t = input()
print(solve(s,t))

if __name__ == '__main__':
    solve()