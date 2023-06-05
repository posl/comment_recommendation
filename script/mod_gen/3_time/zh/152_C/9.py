def solve():
    n = int(input())
    p = list(map(int, input().split()))
    s = [0] * n
    s[0] = p[0]
    for i in range(1, n):
        s[i] = min(s[i - 1], p[i])
    cnt = 0
    for i in range(n):
        if p[i] <= s[i]:
            cnt += 1
    print(cnt)
solve()
