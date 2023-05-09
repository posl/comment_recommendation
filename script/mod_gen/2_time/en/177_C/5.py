def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(N):
        ans += A[i]*A[i]
        ans %= MOD
    for i in range(N):
        for j in range(i+1, N):
            ans += 2*A[i]*A[j]
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()