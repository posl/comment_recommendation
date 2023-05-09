def main():
    N, M = map(int, input().split())
    #print(N, M)
    X = [[0] * N for _ in range(N)] # 2次元配列の初期化
    for i in range(M):
        k = list(map(int, input().split()))
        #print(k)
        for j in range(1, k[0]+1):
            for l in range(j+1, k[0]+1):
                X[k[j]-1][k[l]-1] = 1
                X[k[l]-1][k[j]-1] = 1
    #print(X)
    for i in range(N):
        for j in range(N):
            if X[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()