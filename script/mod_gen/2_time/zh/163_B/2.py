def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        return -1
    else:
        return N - sum(A)
print(solve())
