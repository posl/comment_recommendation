def main():
    N = int(input())
    data = []
    for i in range(N):
        x,y,p = map(int,input().split())
        data.append([x,y,p])
    data.sort(key=lambda x:x[2])
    dp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if data[i][2] * (abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1])) >= data[j][2]:
                dp[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    print(max(dp[i][j] for i in range(N) for j in range(N)))
