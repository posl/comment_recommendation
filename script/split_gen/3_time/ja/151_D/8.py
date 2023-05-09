def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    dist = [[float("inf")]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            if i == 0 and j == 0:
                dist[i][j] = 0
            if i > 0:
                dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
            if j > 0:
                dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if S[i][j] == "#":
                continue
            if i < H-1:
                dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
            if j < W-1:
                dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            ans = max(ans, dist[i][j])
    print(ans)
