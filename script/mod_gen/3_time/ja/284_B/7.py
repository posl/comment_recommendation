def main():
    # 1行目の入力
    T = int(input())
    # T回のループ
    for i in range(T):
        # 2行目の入力
        N = int(input())
        # 3行目の入力
        A = list(map(int, input().split()))
        # 奇数の数をカウントする変数
        count = 0
        # N回のループ
        for j in range(N):
            # 奇数ならカウントする
            if A[j] % 2 == 1:
                count += 1
        # 結果の出力
        print(count)

if __name__ == '__main__':
    main()