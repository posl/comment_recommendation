def main():
    #入力
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    #処理
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()