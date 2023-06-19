def solve(N, M):
    if N == 1:
        for i in range(1, M+1):
            print(i)
        return
    for i in range(1, M+1):
        for j in solve(N-1, M):
            print(i, *j)
N, M = map(int, input().split())
solve(N, M)
