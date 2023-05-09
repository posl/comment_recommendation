def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-K):
        ans += max(A[i]-X, 0)
    for i in range(N-K, N):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()