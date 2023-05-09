def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-K+1):
        ans += A[i] * (N-i-K+1)
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()