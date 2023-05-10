def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    S = sum(A)
    k = 0
    while X > S:
        X -= S
        k += N
    for i in range(N):
        X -= A[i]
        k += 1
        if X < 0:
            break
    print(k)
