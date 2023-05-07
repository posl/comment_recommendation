def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [tuple(map(int, input().split())) for _ in range(Q)]
    # ACが出現する場所を記録
    AC = [0] * N
    for i in range(N - 1):
        if S[i:i + 2] == 'AC':
            AC[i + 1] = 1
    # ACが出現した場所の累積和を求める
    AC_cumsum = [0] * (N + 1)
    for i in range(1, N + 1):
        AC_cumsum[i] = AC_cumsum[i - 1] + AC[i - 1]
    for l, r in LR:
        print(AC_cumsum[r - 1] - AC_cumsum[l - 1])
