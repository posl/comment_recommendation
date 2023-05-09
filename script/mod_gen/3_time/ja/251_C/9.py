def main():
    n = int(input())
    a = [input().split() for _ in range(n)]
    b = []
    for i in range(n):
        if a[i][0] not in b:
            b.append(a[i][0])
    c = []
    for i in range(n):
        if a[i][0] in b:
            c.append(a[i])
    d = []
    for i in range(len(c)):
        d.append(c[i][1])
    e = []
    for i in range(len(c)):
        e.append(int(c[i][1]))
    f = []
    for i in range(len(c)):
        if e[i] == max(e):
            f.append(i)
    print(f[0] + 1)

if __name__ == '__main__':
    main()