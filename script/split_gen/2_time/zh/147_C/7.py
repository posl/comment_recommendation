def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            p, q = map(int, input().split())
            x[i].append(p)
            y[i].append(q)
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j]):
                    if i >> (x[j][k] - 1) & 1 != y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)
