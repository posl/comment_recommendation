def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - X * K)
        K = max(0, K - A[i] // X)
    print(ans)

if __name__ == '__main__':
    main()