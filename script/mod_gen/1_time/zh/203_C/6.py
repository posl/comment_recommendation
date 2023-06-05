def solve():
    n, k = map(int, input().split())
    AB = []
    for _ in range(n):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort()
    now = 0
    for a, b in AB:
        if a - now > k:
            break
        k += b - (a - now)
        now = a
    print(now + k)
solve()
