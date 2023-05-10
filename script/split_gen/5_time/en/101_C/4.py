def problems101_c():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-K):
        if A[i] < A[i+K]:
            ans += 1
    print(ans)
