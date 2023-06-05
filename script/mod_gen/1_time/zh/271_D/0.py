def dfs(i, sum):
    if i == n:
        if sum == S:
            return True
        else:
            return False
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum + a[i]):
        return True
    return False
n, S = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

if __name__ == '__main__':
    dfs()