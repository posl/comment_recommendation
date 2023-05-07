def solve():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S-1:] + A[R-1:Q] + A[P-1:R-1]
    print(*B)
