def main():
    N, M = map(int, input().split())
    N2 = N**2
    dist = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            dist[i][j] = (i**2 + j**2)**0.5
    for i in range(N):
        for j in range(N):
            dist[i][j] = int(dist[i][j])
    # print(dist)
    ans = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if dist[i][j] > M:
                ans[i][j] = -1
            else:
                ans[i][j] = dist[i][j]
    for i in range(N):
        print(' '.join(map(str, ans[i])))
