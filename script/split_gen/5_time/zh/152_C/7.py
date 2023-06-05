def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    m = p[0]
    for i in range(1, n):
        if m >= p[i]:
            ans += 1
            m = p[i]
    print(ans)
