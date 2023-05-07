def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum([(x[i][k] - x[j][k])**2 for k in range(d)])**(1/2)
            if dist.is_integer():
                ans += 1
    print(ans)
