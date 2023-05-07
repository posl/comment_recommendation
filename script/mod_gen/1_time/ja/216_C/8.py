def main():
    N = int(input())
    # 2進数に変換
    N = bin(N)[2:]
    # 2進数の桁数
    N_len = len(N)
    # 答え
    ans = ''
    # 2進数の最下位桁から順に処理
    for i in range(N_len):
        # 下からi桁目の数字
        d = N[N_len-i-1]
        # 1の場合
        if d == '1':
            # 2のi乗
            ans += 'A'*(i+1)
            # 2のi乗-1
            ans += 'B'
        # 0の場合
        else:
            # 2のi乗-1
            ans += 'A'
    # 末尾のBを削除
    ans = ans[:-1]
    print(ans)

if __name__ == '__main__':
    main()