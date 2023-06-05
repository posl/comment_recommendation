def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        # i: start point
        # j: end point
        j = i
        s = 0
        t = 0
        while True:
            j = p[j] - 1
            s += c[j]
            t += 1
            if j == i:
                break
            if t == k:
                break
        if s > 0:
            u = s * (k // t - 1)
            ans = max(ans, u + s)
        else:
            ans = max(ans, s)
    print(ans)
