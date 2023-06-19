def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = [0] * n
    min_a = [0] * n
    max_a[0] = a[0]
    min_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])
        min_a[i] = min(min_a[i - 1], a[i])
    ans = 0
    for i in range(n):
        if min_a[i] < p and max_a[i] > r:
            ans += 1
    print(ans)
