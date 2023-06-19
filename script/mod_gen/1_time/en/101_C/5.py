def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ret = 0
    for i in range(N-K):
        if A[i] < A[i+K]:
            ret += 1
    print(ret+1)
solve()
