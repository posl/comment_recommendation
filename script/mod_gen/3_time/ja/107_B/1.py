def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if "#" in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        d = ""
        for j in range(len(b)):
            d += b[j][i]
        if "#" in d:
            c.append(d)
    for i in range(len(c)):
        print(c[i])

if __name__ == '__main__':
    main()