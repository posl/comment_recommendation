def main():
    N = int(input())
    A = [input() for _ in range(N)]
    ans = ""
    for i in range(N):
        for j in range(N):
            ans += A[i][j]
            if i == N-1:
                ans += A[0][j]
            else:
                ans += A[i+1][j]
            if j == N-1:
                ans += A[i][0]
            else:
                ans += A[i][j+1]
            if i == 0:
                ans += A[N-1][j]
            else:
                ans += A[i-1][j]
            if j == 0:
                ans += A[i][N-1]
            else:
                ans += A[i][j-1]
    print(max(ans))
