def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append(a[i] / b[i])
    c = [x for _, x in sorted(zip(c, b), reverse=True)]
    ans = 0
    for i in range(n):
        if w >= c[i]:
            ans += c[i] * a[i]
            w -= c[i]
        else:
            ans += w * a[i]
            break
    print(int(ans))
