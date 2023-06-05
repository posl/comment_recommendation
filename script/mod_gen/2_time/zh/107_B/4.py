def problems107_b():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        t = []
        for j in range(len(b)):
            t.append(b[j][i])
        if '#' in t:
            c.append(t)
    for i in range(len(c)):
        print(''.join(c[i]))

if __name__ == '__main__':
    problems107_b()