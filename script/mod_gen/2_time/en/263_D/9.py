def main():
    # Read input
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # Initialize
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # Compute
    ans = 10 ** 20
    for i in range(N + 1):
        if L * i <= S[i] <= R * i:
            ans = min(ans, S[i] + max(0, L * (N - i) - S[N] + S[i]))
            ans = min(ans, S[i] + max(0, R * (N - i) - S[N] + S[i]))
    print(ans)

if __name__ == '__main__':
    main()