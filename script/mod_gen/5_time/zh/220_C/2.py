def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    total = sum(A)
    if X <= total:
        print(0)
        return
    if X % total == 0:
        print(N * (X // total))
        return
    X = X % total
    total = 0
    for i in range(N):
        total += A[i]
        if total > X:
            print(N + i + 1)
            return
solve()
