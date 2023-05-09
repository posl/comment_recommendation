def main():
    # 標準入力から H, W を取得する
    H, W = map(int, input().split())
    # 標準入力から C_{i,j} を取得する
    C = [input() for i in range(H)]
    # X を初期化する
    X = [0] * W
    # X を求める
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    # X を出力する
    print(*X)

if __name__ == '__main__':
    main()