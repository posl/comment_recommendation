def main():
    # H 行 W 列のマス目があり、各マスにはコマが置かれているか、何も置かれていないかのどちらかです。
    # マス目の状態は H 個の長さ W の文字列 S_1, S_2, ..., S_H によって表され、
    # S_i の j 文字目が # のとき上から i 行目かつ左から j 列目のマスにはコマが置かれていることを、
    # S_i の j 文字目が . のとき上から i 行目かつ左から j 列目のマスには何も置かれていないことを表しています。
    # マス目上のマスのうち、コマが置かれているようなものの個数を求めてください。
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()