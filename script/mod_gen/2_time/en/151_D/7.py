def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    #print(S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(H):
                for l in range(W):
                    if S[k][l] == '#':
                        continue
                    dist = [[-1 for m in range(W)] for n in range(H)]
                    dist[i][j] = 0
                    q = []
                    q.append([i, j])
                    while len(q) > 0:
                        x, y = q.pop(0)
                        if x > 0:
                            if S[x - 1][y] == '.' and dist[x - 1][y] == -1:
                                q.append([x - 1, y])
                                dist[x - 1][y] = dist[x][y] + 1
                        if x < H - 1:
                            if S[x + 1][y] == '.' and dist[x + 1][y] == -1:
                                q.append([x + 1, y])
                                dist[x + 1][y] = dist[x][y] + 1
                        if y > 0:
                            if S[x][y - 1] == '.' and dist[x][y - 1] == -1:
                                q.append([x, y - 1])
                                dist[x][y - 1] = dist[x][y] + 1
                        if y < W - 1:
                            if S[x][y + 1] == '.' and dist[x][y + 1] == -1:
                                q.append([x, y + 1])
                                dist[x][y + 1] = dist[x][y] + 1
                    #print(dist)
                    ans = max(ans, dist[k][l])
    print(ans)

if __name__ == '__main__':
    main()