def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans = max(ans, dfs(p, i))
    print(ans)
