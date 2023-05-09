def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    b = []
    for i in range(h):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b)):
        if not '.' in b[i]:
            c.append(i)
    d = []
    for i in range(w):
        if not '.' in [b[j][i] for j in range(len(b))]:
            d.append(i)
    for i in range(len(b)):
        e = ''
        for j in range(w):
            if not j in d:
                e += b[i][j]
        print(e)

if __name__ == '__main__':
    main()