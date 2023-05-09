def dfs(arr, n, m):
    if len(arr) == n:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, m+1):
        if len(arr) == 0 or arr[-1] < i:
            arr.append(i)
            dfs(arr, n, m)
            arr.pop()

if __name__ == '__main__':
    dfs()