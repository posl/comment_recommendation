def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x, y: x + y, a, b))
    d = sorted([(a[i], b[i], c[i], i + 1) for i in range(n)], reverse=True)
    e = d[:x]
    f = sorted(d[x:x + y], reverse=True)
    g = sorted(d[x + y:x + y + z], reverse=True)
    h = set([e[i][3] for i in range(len(e))])
    h |= set([f[i][3] for i in range(len(f))])
    h |= set([g[i][3] for i in range(len(g))])
    for i in sorted(h):
        print(i)

if __name__ == '__main__':
    main()