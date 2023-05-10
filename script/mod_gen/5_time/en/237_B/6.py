def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(w):
        b.append([])
        for j in range(h):
            b[i].append(a[j][i])
    for i in range(w):
        print(' '.join(map(str, b[i])))

if __name__ == '__main__':
    main()