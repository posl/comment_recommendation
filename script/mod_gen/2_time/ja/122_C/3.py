def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    AC = [0] * N
    for i in range(N-1):
        if S[i:i+2] == 'AC':
            AC[i+1] = 1
    AC_sum = [0] * (N+1)
    for i in range(N):
        AC_sum[i+1] = AC_sum[i] + AC[i]
    for l, r in LR:
        print(AC_sum[r-1] - AC_sum[l-1])

if __name__ == '__main__':
    main()