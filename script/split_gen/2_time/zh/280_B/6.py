def solve():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    for i in range(N-1):
        A[i] = S[i] + A[i-1]
    A[N-1] = S[N-1] + A[N-2]
    print(' '.join(map(str, A)))
    
solve()
