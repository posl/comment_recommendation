def dfs(i, sum):
    if i == N:
        return sum == S
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + A[i]):
        return True
    return False
N, S = map(int, input().split())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)
