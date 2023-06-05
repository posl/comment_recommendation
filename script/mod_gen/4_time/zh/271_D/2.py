def dfs(i, sum):
    if i == n:
        return sum == s
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False
n, s = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

if __name__ == '__main__':
    dfs()