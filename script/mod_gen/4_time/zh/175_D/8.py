def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        s = 0
        v = i
        for j in range(k):
            v = p[v] - 1
            s += c[v]
            ans = max(ans, s)
            if v == i:
                break
    print(ans)
solve()
