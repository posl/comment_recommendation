def main():
    n, m = map(int, input().split())
    a = [0] * n
    def dfs(i, x):
        if i == n:
            print(" ".join(map(str, a)))
        else:
            for y in range(x + 1, m + 1):
                a[i] = y
                dfs(i + 1, y)
    dfs(0, 0)
