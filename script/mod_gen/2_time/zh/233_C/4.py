def main():
    N,X = map(int, input().split())
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        a.append(L[i][1:])
    print(L)
    print(a)

if __name__ == '__main__':
    main()