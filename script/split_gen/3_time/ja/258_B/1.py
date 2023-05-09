def main():
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, A[i][j] + A[(i+1)%N][j] + A[(i-1)%N][j] + A[i][(j+1)%N] + A[i][(j-1)%N] + A[(i+1)%N][(j+1)%N] + A[(i+1)%N][(j-1)%N] + A[(i-1)%N][(j+1)%N] + A[(i-1)%N][(j-1)%N])
    print(ans)
