def solve():
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input())))
    print(matrix)
    # 从上到下，从左到右
    def check(x, y):
        if x < 0 or x >= N or y < 0 or y >= N:
            return False
        return True
    def dfs(x, y, num, times):
        if times == N:
            return num
        if not check(x, y):
            return num
        num = num * 10 + matrix[x][y]
        ans = 0
        ans = max(ans, dfs(x+1, y, num, times+1))
        ans = max(ans, dfs(x-1, y, num, times+1))
        ans = max(ans, dfs(x, y+1, num, times+1))
        ans = max(ans, dfs(x, y-1, num, times+1))
        ans = max(ans, dfs(x+1, y+1, num, times+1))
        ans = max(ans, dfs(x-1, y-1, num, times+1))
        ans = max(ans, dfs(x+1, y-1, num, times+1))
        ans = max(ans, dfs(x-1, y+1, num, times+1))
        return ans
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, dfs(i, j, 0, 0))
    print(ans)
solve()
