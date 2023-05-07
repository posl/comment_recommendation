def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                P = S[i]
                Q = S[j] - S[i]
                R = S[k] - S[j]
                S_ = S[N] - S[k]
                ans = min(ans, max(P, Q, R, S_) - min(P, Q, R, S_))
    print(ans)

if __name__ == '__main__':
    main()