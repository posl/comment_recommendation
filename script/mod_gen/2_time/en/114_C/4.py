def dfs(n, x):
    if n > N:
        return 0
    if 7 in x and 5 in x and 3 in x:
        ans = 1
    else:
        ans = 0
    for i in [3, 5, 7]:
        ans += dfs(10 * n + i, x | {i})
    return ans
N = int(input())
print(dfs(0, set()))

if __name__ == '__main__':
    dfs()