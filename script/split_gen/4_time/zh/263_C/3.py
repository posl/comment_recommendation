def main():
    n,m = map(int, input().split())
    a = [0]*n
    def dfs(i, x):
        if i == n:
            print(*a)
            return
        for j in range(x+1, m+1):
            a[i] = j
            dfs(i+1, j)
    dfs(0,0)
