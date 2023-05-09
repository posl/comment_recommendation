def dfs(city, time, visited, n):
    if len(visited) == n:
        return 1 if time == k else 0
    ret = 0
    for i in range(1, n):
        if not i in visited:
            ret += dfs(i, time+t[city][i], visited+[i], n)
    return ret
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, 0, [0], n))

if __name__ == '__main__':
    dfs()