def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int, input().split())))
    for i in range(n):
        a.append(k[i][1:])
    b = []
    for i in range(n):
        for j in range(k[i][0]):
            b.append(a[i][j])
    c = sorted(b)
    d = []
    for i in range(len(c)):
        if c[i] == c[i-1]:
            d.append(c[i])
    e = set(d)
    f = list(e)
    print(len(f))
