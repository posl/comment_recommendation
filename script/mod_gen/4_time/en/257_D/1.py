def main():
    N = int(input())
    trampolines = []
    for i in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    # print(trampolines)
    def can_move(i, j):
        x1, y1, p1 = trampolines[i]
        x2, y2, p2 = trampolines[j]
        return p1 * S >= abs(x1 - x2) + abs(y1 - y2)
    def dfs(i):
        if i in visited:
            return
        visited.add(i)
        for j in range(N):
            if can_move(i, j):
                dfs(j)
    ans = 0
    for S in range(1, N + 1):
        visited = set()
        for i in range(N):
            if i in visited:
                continue
            dfs(i)
            ans = max(ans, S)
    print(ans)

if __name__ == '__main__':
    main()