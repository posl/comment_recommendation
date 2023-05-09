def dfs(lst, n, m):
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, m+1):
        if len(lst) > 0 and lst[-1] >= i:
            continue
        dfs(lst+[i], n, m)
n, m = map(int, input().split())
dfs([], n, m)

if __name__ == '__main__':
    dfs()