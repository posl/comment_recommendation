def main():
    # 標準入力から値を取得する
    N, X = map(int, input().split())
    S = list(input())
    
    # 処理
    ans = X
    for i in range(N):
        if S[i] == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)
    # 出力
    print(ans)

if __name__ == '__main__':
    main()