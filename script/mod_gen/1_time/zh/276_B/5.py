def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    a.sort()
    b = []
    for i in range(n):
        b.append([])
    for i in range(m):
        b[a[i][0]-1].append(a[i][1])
        b[a[i][1]-1].append(a[i][0])
    for i in range(n):
        b[i].sort()
    for i in range(n):
        print(len(b[i]), end = " ")
        for j in range(len(b[i])):
            print(b[i][j], end = " ")
        print()

if __name__ == '__main__':
    main()