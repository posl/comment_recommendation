def main():
    S = input()
    N = len(S)
    S = S[::-1]
    M = 2019
    R = [0] * M
    R[0] = 1
    n = 0
    t = 1
    for i in range(N):
        n += int(S[i]) * t
        n %= M
        t *= 10
        t %= M
        R[n] += 1
    ans = 0
    for i in range(M):
        ans += R[i] * (R[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()