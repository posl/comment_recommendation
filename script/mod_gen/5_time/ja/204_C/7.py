def main():
    # 標準入力の取得
    n, m = map(int, input().split())
    # 都市の組み合わせの数を格納する変数
    ans = 0
    # 都市の組み合わせの数を計算
    ans = n * (n - 1) // 2
    # 都市の組み合わせの数を出力
    print(ans)

if __name__ == '__main__':
    main()