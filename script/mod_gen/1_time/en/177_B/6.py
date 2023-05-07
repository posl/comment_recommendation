def solve(s, t):
    sl = len(s)
    tl = len(t)
    res = 1000
    for i in range(sl - tl + 1):
        tmp = 0
        for j in range(tl):
            if s[i+j] != t[j]:
                tmp += 1
        res = min(res, tmp)
    return res
s = input()
t = input()
print(solve(s, t))

if __name__ == '__main__':
    solve()