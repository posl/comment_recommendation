def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000000000000
    for i in range(2 ** d):
        t = 0
        s = 0
        for j in range(d):
            if i >> j & 1:
                t += p[j]
                s += 100 * (j + 1) * p[j] + c[j]
        if g <= s:
            ans = min(ans, t)
        else:
            for j in range(d - 1, -1, -1):
                if i >> j & 1:
                    continue
                for k in range(p[j]):
                    if g <= s:
                        break
                    t += 1
                    s += 100 * (j + 1)
            ans = min(ans, t)
    print(ans)
