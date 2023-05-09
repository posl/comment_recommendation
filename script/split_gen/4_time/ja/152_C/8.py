def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = 1
    for i in range(n):
        if m >= p[i]:
            ans += 1
        m = min(m, p[i])
    print(ans)
