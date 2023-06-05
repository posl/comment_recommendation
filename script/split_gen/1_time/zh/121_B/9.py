def solve():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        tmp += C
        if tmp > 0:
            cnt += 1
    print(cnt)
