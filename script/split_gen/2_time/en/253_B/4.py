def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                start = (i, j)
                break
        else:
            continue
        break
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if S[i][j] == "o":
                goal = (i, j)
                break
        else:
            continue
        break
    print(abs(start[0] - goal[0]) + abs(start[1] - goal[1]))
