def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # a[0]を使う場合の最大値
    dp0 = [0] * n
    dp0[0] = a[0] * p
    for i in range(1, n):
        dp0[i] = max(dp0[i - 1], a[i] * p)
    # a[0]とa[1]を使う場合の最大値
    dp1 = [0] * n
    dp1[1] = dp0[0] + a[1] * q
    for i in range(2, n):
        dp1[i] = max(dp1[i - 1], dp0[i - 1] + a[i] * q)
    # a[0]とa[1]とa[2]を使う場合の最大値
    dp2 = [0] * n
    dp2[2] = dp1[1] + a[2] * r
    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp1[i - 1] + a[i] * r)
    # a[0]とa[1]とa[2]とa[3]を使う場合の最大値
    dp3 = [0] * n
    dp3[3] = dp2[2]
    for i in range(4, n):
        dp3[i] = max(dp3[i - 1], dp2[i - 1])
    # a[0]とa[1]とa[2]とa[3]とa[4]を使う場合の最大値
    dp4 = [0] * n
    dp4[4] = dp3[3]
    for i in range(5, n):
        dp4[i] = max(dp4[i - 1], dp3[i - 1])
    # a[0]とa[1]とa[2]とa[3]とa[4]とa[5]を使う場合の最大

if __name__ == '__main__':
    main()