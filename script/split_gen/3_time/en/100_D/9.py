def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]
    ans = -1e18
    for i in range(8):
        tmp = 0
        for j in range(n):
            tmp += max([cakes[j][k] if i >> k & 1 else -cakes[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)
