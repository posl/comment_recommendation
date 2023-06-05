def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K * 2 >= N:
        print('Yes')
        return
    for i in range(K, N):
        if A[i - K] >= A[i]:
            print('Yes')
            return
    print('No')
solve()
