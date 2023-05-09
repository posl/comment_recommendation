def main():
    #入力
    S = [input() for i in range(9)]
    #print(S)
    #初期化
    cnt = 0
    #処理
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                if i+1 < 9 and j+1 < 9 and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                    cnt += 1
    #出力
    print(cnt)

if __name__ == '__main__':
    main()