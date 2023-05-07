def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    d = {}
    for i in range(N+1):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    ans = 0
    for i in range(N+1):
        if A[i] - K in d:
            ans += d[A[i] - K]
    print(ans)

if __name__ == '__main__':
    main()