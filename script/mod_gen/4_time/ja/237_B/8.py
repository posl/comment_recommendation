def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    #print(a)
    b = []
    for i in range(w):
        b.append([])
        for j in range(h):
            b[i].append(a[j][i])
    #print(b)
    for i in range(w):
        print(*b[i])

if __name__ == '__main__':
    main()