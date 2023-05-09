def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    b = []
    for i in range(H):
        if a[i].count('#') != 0:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        if [j[i] for j in b].count('#') != 0:
            c.append([j[i] for j in b])
    d = []
    for i in range(len(c[0])):
        d.append(''.join([j[i] for j in c]))
    for i in d:
        print(i)

if __name__ == '__main__':
    main()