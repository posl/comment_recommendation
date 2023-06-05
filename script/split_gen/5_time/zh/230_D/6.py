def solve(n, d, lr):
    lr.sort()
    ans = 0
    p = 0
    for i in range(n):
        l, r = lr[i]
        if p < l:
            p = l
        if r - p + 1 < d:
            continue
        ans += 1
        p += d
    return ans
n, d = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, d, lr))
