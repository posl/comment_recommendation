def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[0:K]))
