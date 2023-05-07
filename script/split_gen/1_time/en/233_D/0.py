def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n + 1):
        c[i] = b[i] - k
    d = [0] * (n + 1)
    for i in range(n + 1):
        d[i] = c[i] - i
    e = {}
    for i in range(n + 1):
        if d[i] in e:
            e[d[i]] += 1
        else:
            e[d[i]] = 1
    ans = 0
    for i in e:
        ans += e[i] * (e[i] - 1) // 2
    print(ans)
