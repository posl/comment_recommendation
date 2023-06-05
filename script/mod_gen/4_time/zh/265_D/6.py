def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])
    min_a = [0] * n
    min_a[0] = a[0]
    for i in range(1, n):
        min_a[i] = min(min_a[i - 1], a[i])
    ans = 0
    for i in range(n):
        if min_a[i] == a[i] and max_a[i] == a[i]:
            continue
        ans = max(ans, (p - 1) * a[i] + q * (max_a[i] - a[i]) + r * (a[i] - min_a[i]))
    print(ans)
solve()
