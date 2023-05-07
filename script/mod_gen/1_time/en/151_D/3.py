def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            stack = [[i,j]]
            visited = [[False for _ in range(W)] for _ in range(H)]
            visited[i][j] = True
            while len(stack) > 0:
                x, y = stack.pop()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= H or ny < 0 or ny >= W:
                        continue
                    if visited[nx][ny]:
                        continue
                    if S[nx][ny] == '#':
                        continue
                    visited[nx][ny] = True
                    stack.append([nx, ny])
            tmp = 0
            for k in range(H):
                for l in range(W):
                    if visited[k][l]:
                        tmp += 1
            ans = max(ans, tmp)
    print(ans-1)

if __name__ == '__main__':
    main()