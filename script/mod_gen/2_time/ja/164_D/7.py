def main():
    S = input()
    mod = 2019
    # 各桁の数字を取り出してリストにする
    L = [int(s) for s in S]
    # 2019の倍数の個数
    ans = 0
    # 2019の倍数の個数を求める
    for i in range(len(L)):
        for j in range(i, len(L)):
            # i文字目からj文字目までの整数を求める
            num = 0
            for k in range(i, j+1):
                num = num * 10 + L[k]
            if num % mod == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()