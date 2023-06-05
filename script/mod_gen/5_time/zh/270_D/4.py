def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if i == 0:
            ans += A[i] * (N // A[i])
            N = N % A[i]
        else:
            if N >= A[i]:
                ans += (N - A[i]) + 1
                N = A[i] - 1
    print(ans)

if __name__ == '__main__':
    main()