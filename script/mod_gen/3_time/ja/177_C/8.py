def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    # Aの累積和
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    for i in range(1,N):
        ans += A[i] * (S[-1] - S[i])
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()