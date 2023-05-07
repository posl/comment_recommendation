def main():
    K = int(input())
    # 2進数の桁数
    n = 1
    # 2進数の桁数が n のときの 0,2 のみからなる正整数の個数
    cnt = 1
    while cnt < K:
        n += 1
        cnt *= 2
    # 2進数の桁数が n のときの 0,2 のみからなる正整数の最初の値
    start = 2 ** (n-1)
    # 2進数の桁数が n のときの 0,2 のみからなる正整数の最後の値
    end = 2 ** n - 1
    # 2進数の桁数が n のときの 0,2 のみからなる正整数の最初の値から K 番目の値を求める
    ans = start + K - cnt // 2 - 1
    print(ans)

if __name__ == '__main__':
    main()