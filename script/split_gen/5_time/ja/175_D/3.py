def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x] - 1
            s += c[x]
            t += 1
            if x == i:
                break
            if t >= k:
                break
        if c[x] > 0:
            u = (k - t) // t
            s += s * u
            t += t * u
            v = 0
            while v < k - t:
                x = p[x] - 1
                s += c[x]
                v += 1
        ans = max(ans, s)
    print(ans)
