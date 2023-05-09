def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # ひとまず、#がある行と列を抽出
    rows = []
    cols = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                rows.append(i)
                cols.append(j)
    # 重複を除く
    rows = list(set(rows))
    cols = list(set(cols))
    # print(rows)
    # print(cols)
    # 抽出した行と列を使って、新しい行列を作成
    for i in range(len(rows)):
        for j in range(len(cols)):
            print(S[rows[i]][cols[j]], end="")
        print("")

if __name__ == '__main__':
    main()