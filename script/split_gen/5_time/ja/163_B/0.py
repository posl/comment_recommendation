def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum <= N:
        print(N - sum)
    else:
        print(-1)
