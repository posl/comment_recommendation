def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    B = [list(map(int, input().split())) for i in range(N)]
    A.sort()
    B.sort()
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                print("No")
                return
    print("Yes")
