def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    pos = [1, 1]
    visited = [[False for _ in range(W)] for _ in range(H)]
    while True:
        visited[pos[0]-1][pos[1]-1] = True
        if G[pos[0]-1][pos[1]-1] == "U":
            if pos[0] == 1:
                break
            else:
                pos[0] -= 1
        elif G[pos[0]-1][pos[1]-1] == "D":
            if pos[0] == H:
                break
            else:
                pos[0] += 1
        elif G[pos[0]-1][pos[1]-1] == "L":
            if pos[1] == 1:
                break
            else:
                pos[1] -= 1
        elif G[pos[0]-1][pos[1]-1] == "R":
            if pos[1] == W:
                break
            else:
                pos[1] += 1
        if visited[pos[0]-1][pos[1]-1] == True:
            pos = [-1, -1]
            break
    print(" ".join(map(str, pos)))
