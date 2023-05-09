def main():
    N = int(input())
    ans = [[1] * (i+1) for i in range(N)]
    for i in range(2,N):
        for j in range(1,i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    for i in range(N):
        print(*ans[i])
