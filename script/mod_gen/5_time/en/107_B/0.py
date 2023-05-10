def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        if '#' in [b[j][i] for j in range(len(b))]:
            c.append([b[j][i] for j in range(len(b))])
    for i in range(len(c)):
        print(''.join(c[i]))

if __name__ == '__main__':
    main()