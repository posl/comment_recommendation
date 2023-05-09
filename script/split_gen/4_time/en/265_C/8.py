def main():
    H,W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(input())
    visited = [[False for _ in range(W)] for _ in range(H)]
    i,j = 0,0
    while True:
        if visited[i][j]:
            print(-1)
            break
        visited[i][j] = True
        if G[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1
