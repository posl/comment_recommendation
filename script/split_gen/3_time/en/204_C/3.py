def main():
    N, M = map(int, input().split())
    road = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1][B-1] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 0:
                continue
            for k in range(N):
                if road[j][k] == 1:
                    road[i][k] = 1
    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                ans += 1
    print(ans)
