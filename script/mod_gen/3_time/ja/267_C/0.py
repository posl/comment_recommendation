def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(M, N + 1):
        ans = max(ans, S[i] - S[i - M])
    print(ans)

if __name__ == '__main__':
    main()