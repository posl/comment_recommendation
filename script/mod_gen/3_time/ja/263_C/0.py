def dfs(i, n, m, a):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m + 1):
        a[i] = j
        dfs(i + 1, n, m, a)
n, m = map(int, input().split())
a = [0] * n
dfs(0, n, m, a)

if __name__ == '__main__':
    dfs()