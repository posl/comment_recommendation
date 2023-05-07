def main():
    N, X, Y = map(int, input().split())
    # レベル 1 の青い宝石の個数を求める
    def get_blue(N):
        if N == 1:
            return 0
        elif N == 2:
            return X
        else:
            return Y * get_blue(N - 1) + get_blue(N - 2)
    # レベル 1 の青い宝石の個数を出力
    print(get_blue(N))

if __name__ == '__main__':
    main()