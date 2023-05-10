def main():
    # 標準入力を取得
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 一番人気のジェットコースターに乗ることができる人の数を求める
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    # 結果を出力
    print(count)

if __name__ == '__main__':
    main()