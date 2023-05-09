def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i]
        ans %= 10**9+7
    ans *= N * (N-1) // 2
    ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()