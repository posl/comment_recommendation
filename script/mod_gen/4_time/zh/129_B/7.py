def solve():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100 * 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        ans = min(ans, abs(s1 - s2))
    print(ans)
solve()
