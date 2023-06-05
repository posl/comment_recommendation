def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        sum = C
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum > 0:
            cnt += 1
    print(cnt)
