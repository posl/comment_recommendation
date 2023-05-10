def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    city = [[] for _ in range(N)]
    for i in range(M):
        city[P_Y[i][0] - 1].append([P_Y[i][1], i])
    for i in range(N):
        city[i].sort()
    ans = [0] * M
    for i in range(N):
        for j in range(len(city[i])):
            ans[city[i][j][1]] = str(i + 1).zfill(6) + str(j + 1).zfill(6)
    for i in range(M):
        print(ans[i])
