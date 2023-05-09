def main():
    n, m = map(int, input().split())
    a = [0] * n
    def dfs(i):
        if i == n:
            print(' '.join(map(str, a)))
        else:
            for j in range(1, m + 1):
                a[i] = j
                dfs(i + 1)
    dfs(0)
