def dfs(i, sum):
    if i == n:
        if sum == s:
            return True
        else:
            return False
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum+a[i]):
        ans.append("T")
        return True
    if dfs(i+1, sum+b[i]):
        ans.append("H")
        return True
    return False
n, s = map(int, input().split())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = []
