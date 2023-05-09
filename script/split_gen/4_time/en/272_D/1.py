def main():
    N, M = map(int, input().split())
    if N == 1:
        print(0)
        return
    if M == 1:
        for i in range(N):
            print(i+1)
        return
    dist = [[float('inf') for i in range(N)] for j in range(N)]
    dist[0][0] = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            for k in range(i):
                for l in range(j):
                    if (i-k)**2 + (j-l)**2 == M:
                        dist[i][j] = min(dist[i][j], dist[k][l] + 1)
                    elif (i-k)**2 + (j-l)**2 > M:
                        break
            for k in range(i):
                if (i-k)**2 + j**2 == M:
                    dist[i][j] = min(dist[i][j], dist[k][j] + 1)
                elif (i-k)**2 + j**2 > M:
                    break
            for k in range(j):
                if i**2 + (j-k)**2 == M:
                    dist[i][j] = min(dist[i][j], dist[i][k] + 1)
                elif i**2 + (j-k)**2 > M:
                    break
            if i**2 + j**2 == M:
                dist[i][j] = min(dist[i][j], 1)
    for i in range(N):
        for j in range(N):
            if dist[i][j] == float('inf'):
                dist[i][j] = -1
    for i in range(N):
        print(*dist[i])
