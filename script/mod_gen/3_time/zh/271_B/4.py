def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ST = []
    for i in range(Q):
        ST.append(list(map(int, input().split())))
    for i in range(Q):
        print(L[ST[i][0]-1][ST[i][1]-1])

if __name__ == '__main__':
    main()