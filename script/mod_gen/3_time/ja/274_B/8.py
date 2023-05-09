def main():
    #入力
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    #print(H, W)
    #print(C)
    #初期化
    X = [0 for i in range(W)]
    #print(X)
    #計算
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[j] += 1
    #出力
    print(*X)

if __name__ == '__main__':
    main()