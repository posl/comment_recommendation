def solve(n, m, edges):
    colors = ['R', 'G', 'B']
    def dfs(i, color):
        colors[i] = color
        for j in edges[i]:
            if colors[j] == color:
                return False
            if colors[j] == None and not dfs(j, 'R' if color == 'G' else 'G'):
                return False
        return True
    res = 0
    for i in range(n):
        colors = [None] * n
        if dfs(i, 'R'):
            res += 1
        colors = [None] * n
        if dfs(i, 'G'):
            res += 1
        colors = [None] * n
        if dfs(i, 'B'):
            res += 1
    return res
