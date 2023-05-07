def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()