def problems151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if p[pi] == 0:
            if si == 'AC':
                p[pi] = 1
            else:
                s[pi] += 1
    print(sum(p), sum([p[i] * s[i] for i in range(n)]))
problems151_c()
