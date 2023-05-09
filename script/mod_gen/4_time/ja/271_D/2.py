def dfs(i, sum):
    if i == n:
        if sum == s:
            return True
        else:
            return False
    if dfs(i + 1, sum + a[i]):
        b[i] = 1
        return True
    if dfs(i + 1, sum):
        b[i] = 0
        return True
    return False
n, s = map(int, input().split())
a = []
b = [0] * n
for i in range(n):
    a.append(list(map(int, input().split())))

if __name__ == '__main__':
    dfs()