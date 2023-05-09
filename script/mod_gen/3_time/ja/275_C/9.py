def main():
    #入力
    S = [input() for i in range(9)]
    #座標のリスト
    list = []
    #条件を満たす座標をリストに格納
    for i in range(8):
        for j in range(8):
            if S[i][j] == "#" and S[i+1][j] == "#" and S[i][j+1] == "#" and S[i+1][j+1] == "#":
                list.append([i,j])
    #出力
    print(len(list))

if __name__ == '__main__':
    main()