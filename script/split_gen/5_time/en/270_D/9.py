def solve():
    # Implement solution here
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum(A[0:A.index(N)]) + (N - A[A.index(N) - 1]))
