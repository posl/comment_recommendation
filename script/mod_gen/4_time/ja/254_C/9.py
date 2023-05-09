def main():
    # データ入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # ソート後の配列
    A_sort = sorted(A)
    # 交換回数
    change_count = 0
    # ソート後の配列の要素数分ループ
    for i in range(N):
        # ソート後の配列の要素と元の配列の要素が一致しない場合
        if A_sort[i] != A[i]:
            # 交換回数をカウントアップ
            change_count += 1
    # 交換回数がK以下の場合
    if change_count <= K:
        # Yesを出力
        print("Yes")
    else:
        # Noを出力
        print("No")

if __name__ == '__main__':
    main()