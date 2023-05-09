def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    start = []
    goal = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                start.append((i, j))
                goal.append((i, j))
    ans = 0
    for i in range(len(start)):
        for j in range(len(goal)):
            ans = max(ans, bfs(start[i], goal[j], S))
    print(ans)
