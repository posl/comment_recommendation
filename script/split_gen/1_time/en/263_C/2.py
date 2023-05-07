def main():
    n, m = map(int, input().split())
    a = [0]*n
    def dfs(i):
        if i == n:
            print(*a)
            return
        for j in range(1, m+1):
            if i > 0 and a[i-1] >= j:
                continue
            a[i] = j
            dfs(i+1)
    dfs(0)
