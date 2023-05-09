def main():
    N,K = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(N)]
    B = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(N):
            B[i+1][j+1] = B[i+1][j] + B[i][j+1] - B[i][j] + A[i][j]
    ans = 10**10
    for i in range(N-K+1):
        for j in range(N-K+1):
            tmp = B[i+K][j+K] - B[i+K][j] - B[i][j+K] + B[i][j]
            ans = min(ans,tmp//(K*K))
    print(ans)
