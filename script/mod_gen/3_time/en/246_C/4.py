def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N - K:
            ans += max(A[i], 0)
        else:
            ans += max(A[i] - X, 0)
    print(ans)

if __name__ == '__main__':
    main()