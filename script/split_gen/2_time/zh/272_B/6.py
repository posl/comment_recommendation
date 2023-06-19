def main():
    N, M = map(int, input().split())
    A = [[0] * N for i in range(N)]
    for i in range(M):
        x = list(map(int, input().split()))
        for j in range(x[0]):
            A[x[j+1]-1][i] = 1
    for i in range(N):
        for j in range(i+1, N):
            if sum([A[i][k] * A[j][k] for k in range(M)]) == 0:
                print("No")
                exit()
    print("Yes")
