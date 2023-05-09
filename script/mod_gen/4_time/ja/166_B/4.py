def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for _ in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    s = set()
    for i in range(k):
        for j in range(d[i]):
            s.add(a[i][j])
    print(n - len(s))

if __name__ == '__main__':
    main()