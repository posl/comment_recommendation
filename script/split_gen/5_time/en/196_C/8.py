def solve():
    n = int(input())
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            p = 10 * i + j
            q = 10 * j + i
            if p <= n:
                ans += 1
            if q <= n:
                ans += 1
    print(ans)
