def main():
    # 標準入力から N, K を取得する
    N, K = map(int, input().split())
    # N と K を 3 桁の整数とみなして、部屋番号の合計を計算する
    # N は 1 桁なので 100 を掛ける
    # K は 1 桁なので 10 を掛ける
    print(N * 100 * (N * 100 + K * 10 + K))

if __name__ == '__main__':
    main()