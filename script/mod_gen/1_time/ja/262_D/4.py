def main():
    # 1行目の入力
    N = int(input())
    # 2行目の入力
    A = list(map(int, input().split()))
    # 結果の出力
    print(sum(A) * (2 ** (N - 1)) % 998244353)

if __name__ == '__main__':
    main()