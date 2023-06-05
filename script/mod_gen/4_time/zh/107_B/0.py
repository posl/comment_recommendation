def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        d = []
        for j in range(len(b)):
            d.append(b[j][i])
        if '#' in d:
            c.append(d)
    for i in range(len(c)):
        print(''.join(c[i]))
main()
