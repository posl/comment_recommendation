def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if (A[k][0] == i + 1 and A[k][1] == j + 1) or (A[k][0] == j + 1 and A[k][1] == i + 1):
                    if (B[k][0] == i + 1 and B[k][1] == j + 1) or (B[k][0] == j + 1 and B[k][1] == i + 1):
                        continue
                    else:
                        print("No")
                        return
                elif (B[k][0] == i + 1 and B[k][1] == j + 1) or (B[k][0] == j + 1 and B[k][1] == i + 1):
                    if (A[k][0] == i + 1 and A[k][1] == j + 1) or (A[k][0] == j + 1 and A[k][1] == i + 1):
                        continue
                    else:
                        print("No")
                        return
    print("Yes")
    return
