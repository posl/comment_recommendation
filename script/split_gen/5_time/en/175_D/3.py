def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [x - 1 for x in p]
    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x]
            s += c[x]
            t += 1
            if x == i:
                break
            if t == k:
                break
        if s > 0:
            u = (k - t) // t
            s += s * u
            t += t * u
        for j in range(k - t):
            x = p[x]
            s += c[x]
            ans = max(ans, s)
    print(ans)
