def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    c = [0] * m
    d = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(m):
        c[i], d[i] = map(int, input().split())
    for i in range(2**n):
        p = []
        for j in range(n):
            if (i >> j) & 1:
                p.append(j+1)
        if len(p) == n:
            break
    for i in range(m):
        if (a[i] in p) ^ (b[i] in p):
            print('No')
            exit()
        if (c[i] in p) ^ (d[i] in p):
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()