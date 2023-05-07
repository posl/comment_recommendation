def main():
    import sys
    input = sys.stdin.readline
    # 10^9 + 7
    MOD = 10**9 + 7
    # 文字列入力
    S = input().rstrip()
    # ?の個数
    Q = S.count("?")
    # 3^Q
    Q3 = pow(3, Q, MOD)
    # 3^Qの和
    Q3sum = 0
    # 累積和
    Asum = [0] * (len(S) + 1)
    Bsum = [0] * (len(S) + 1)
    Csum = [0] * (len(S) + 1)
    # 累積和作成
    for i in range(len(S)):
        if S[i] == "A":
            Asum[i + 1] = Asum[i] + 1
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i]
        elif S[i] == "B":
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i] + 1
            Csum[i + 1] = Csum[i]
        elif S[i] == "C":
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i] + 1
        else:
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i]
    # ABC数の和
    ABCsum = 0
    # ?をA,B,Cに置き換える
    for i in range(len(S)):
        if S[i] == "?":
            # ?をAに置き換える場合
            A = Asum[i] + 1
            B = Bsum[i]
            C = Csum[i]
            ABCsum += A * B * C * Q3
            ABCsum %= MOD
            # ?をBに置き換える場合
            A = Asum[i]

if __name__ == '__main__':
    main()