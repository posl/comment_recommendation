def main():
    #input
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #compute
    s = 0
    for i in range(H):
        for j in range(W):
            s += A[i][j]
    if s % (H*W) != 0:
        print(-1)
        return
    s //= (H*W)
    for i in range(H):
        for j in range(W):
            if A[i][j] > s:
                A[i][j] -= s
            else:
                A[i][j] = 0
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                ans += 1
                A[i][j] = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < H and 0 <= ny < W and A[nx][ny] > 0:
                            A[nx][ny] = 0
                            stack.append((nx, ny))
    print(ans)

if __name__ == '__main__':
    main()