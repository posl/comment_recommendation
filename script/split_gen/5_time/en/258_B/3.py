def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                continue
            ans = max(ans, A[i-1][j-1] * 1000 + A[i-1][j] * 100 + A[i-1][j+1] * 10000 + A[i][j-1] * 10 + A[i][j] * 1 + A[i][j+1] * 1000 + A[i+1][j-1] * 100 + A[i+1][j] * 10 + A[i+1][j+1] * 1)
    print(ans)
