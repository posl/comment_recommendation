def main():
    N,M = map(int,input().split())
    k = []
    a = []
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int,input().split())))
    for i in range(M):
        for j in range(k[i]):
            a[i][j] -= 1
    print(a)
    print(k)
    print(N,M)

if __name__ == '__main__':
    main()