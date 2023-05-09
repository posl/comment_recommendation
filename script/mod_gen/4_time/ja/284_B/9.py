def main():
    # Tの入力
    T = int(input())
    # 各テストケースの処理
    for i in range(T):
        # Nの入力
        N = int(input())
        # Aの入力
        A = list(map(int, input().split()))
        # 奇数の数を初期化
        odd = 0
        # Aの要素の数だけ繰り返す
        for j in range(N):
            # Aの要素が奇数なら
            if (A[j] % 2 == 1):
                # 奇数の数をカウントアップ
                odd += 1
        # 答えを出力
        print(odd)

if __name__ == '__main__':
    main()