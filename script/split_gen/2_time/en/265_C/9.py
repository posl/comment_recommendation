def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    #print("H = {} W = {}".format(H, W))
    #print("G = {}".format(G))
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif G[i][j] == 'D':
            if i == H - 1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif G[i][j] == 'R':
            if j == W - 1:
                break
            j += 1
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
    print("{} {}".format(i + 1, j + 1))
