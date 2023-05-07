def dfs(a, n, m):
    if len(a) == n:
        print(" ".join(map(str, a)))
        return
    for i in range(1, m+1):
        if len(a) == 0 or a[-1] < i:
            a.append(i)
            dfs(a, n, m)
            a.pop()
n, m = map(int, input().split())
dfs([], n, m)

if __name__ == '__main__':
    dfs()