def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] + b[i] for i in range(n)]
    d = sorted(range(n), key=lambda i: a[i], reverse=True)
    e = sorted(range(n), key=lambda i: b[i], reverse=True)
    f = sorted(range(n), key=lambda i: c[i], reverse=True)
    g = []
    for i in range(x):
        g.append(d[i])
    for i in range(y):
        g.append(e[i])
    for i in range(z):
        g.append(f[i])
    h = sorted(list(set(g)))
    for i in h:
        print(i+1)

if __name__ == '__main__':
    main()