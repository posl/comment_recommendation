def solve():
    N,M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(M):
                if (A[k] == i+1 and B[k] == j+1) and (C[k] != i+1 or D[k] != j+1):
                    return False
                if (A[k] != i+1 or B[k] != j+1) and (C[k] == i+1 and D[k] == j+1):
                    return False
    return True

if __name__ == '__main__':
    solve()