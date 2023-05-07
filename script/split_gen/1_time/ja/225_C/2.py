def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[(i-1)*7+j for j in range(1, 8)] for i in range(1, 10**100+1)]
    for i in range(10**100-N+1):
        for j in range(7-M+1):
            if A[i][j:j+M] == B[0]:
                for k in range(1, N):
                    if A[i+k][j:j+M] != B[k]:
                        break
                else:
                    print("Yes")
                    return
    print("No")
    return
