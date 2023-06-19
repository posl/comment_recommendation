def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = 0
    for i in range(N):
        m = max(m, abs(A[i] - B[i]))
    if m <= K:
        print('Yes')
    else:
        print('No')
solve()
